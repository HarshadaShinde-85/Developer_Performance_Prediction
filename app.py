from flask import Flask, render_template, request, redirect, session
import sqlite3
import pickle
import random
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client


app = Flask(__name__)
app.secret_key = "secret_key_project"


# LOAD MODEL
model = pickle.load(open("train_model.pkl", "rb"))
print("MODEL TYPE:", type(model))


# DATABASE
def connect_db():
    return sqlite3.connect("users.db")


def create_table():
    conn = connect_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        position TEXT,
        age INTEGER,
        dob TEXT,
        contact TEXT
    )
    """)

    conn.close()


create_table()


# EMAIL FUNCTION
def send_email(receiver_email, subject, message):

    sender_email = "harshushinde852004@gmail.com"
    sender_password = "ubxf jvhg ivow gttq"

    msg = MIMEText(message)

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()


# SMS FUNCTION
def send_sms_otp(mobile, otp):

    account_sid = "ACad06db30860d430dd504ceb58b609900"
    auth_token = "fe4d77ba54d87061f15b740267265d60"

    client = Client(account_sid, auth_token)

    client.messages.create(
        body=f"Verification Code: {otp}",
        from_="+19785477784",
        to="+91" + mobile
    )


# HOME
@app.route("/")
def home():
    return render_template("login.html")


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        position = request.form["position"]
        age = request.form["age"]
        dob = request.form["dob"]
        contact = request.form["contact"]

        conn = connect_db()

        conn.execute("""
        INSERT INTO users(name,email,password,position,age,dob,contact)
        VALUES(?,?,?,?,?,?,?)
        """, (name, email, password, position, age, dob, contact))

        conn.commit()
        conn.close()


        email_message = f"""
Hello {name},

🎉 Your account has been created successfully!

Regards,
Developer Performance Prediction System
"""

        send_email(email, "Account Created Successfully", email_message)

        return redirect("/")

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    conn = connect_db()

    user = conn.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    ).fetchone()

    conn.close()

    if user:
        session["user"] = email
        return redirect("/dashboard")

    return render_template("login.html",
                           error="Invalid Email or Password ❌")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")

#PREDICT
@app.route("/predict", methods=["POST"])
def predict():

    features = [
        "Hours_Coding",
        "Lines_of_Code",
        "Bugs_Found",
        "Bugs_Fixed",
        "AI_Usage_Hours",
        "Sleep_Hours",
        "Cognitive_Load",
        "Task_Success_Rate",
        "Coffee_Intake",
        "Stress_Level",
        "Task_Duration_Hours",
        "Commits",
        "Errors",
        "Complexity"
    ]

    values = [float(request.form[f]) for f in features]

    prediction = model.predict([values])[0]

    return render_template("result.html", prediction=prediction)

        # Optional: convert numeric output to readable label
        if prediction == 0:
            result = "Low Performance ❌"
        elif prediction == 1:
            result = "Medium Performance ⚠️"
        else:
            result = "High Performance ✅"

        return render_template("result.html", prediction=result)

    except Exception as e:
        return f"Prediction Error: {e}"


# FORGOT PASSWORD
@app.route("/forgot")
def forgot():
    return render_template("forgot_password.html")


# SEND OTP
@app.route("/send_otp", methods=["POST"])
def send_otp():

    user_input = request.form["email"]

    conn = connect_db()

    user = conn.execute("""
    SELECT name,email,contact
    FROM users
    WHERE email=? OR contact=?
    """, (user_input, user_input)).fetchone()

    conn.close()

    if not user:
        return "User not registered!"

    name = user[0]

    otp = str(random.randint(1000, 9999))

    session["otp"] = otp
    session["reset_user"] = user_input


    if "@" in user_input:

        message = f"Hello {name}, Your OTP is {otp}"

        send_email(user_input,
                   "Password Reset OTP",
                   message)

    else:

        send_sms_otp(user_input, otp)

    return render_template("verify_otp.html")


# VERIFY OTP
@app.route("/verify_otp", methods=["POST"])
def verify_otp():

    entered_otp = request.form["otp"]

    if entered_otp == session.get("otp"):
        return render_template("new_password.html")

    return render_template("verify_otp.html",
                           error="Invalid OTP ❌")


# UPDATE PASSWORD
@app.route("/update_password", methods=["POST"])
def update_password():

    new_password = request.form["password"]
    user_input = session.get("reset_user")

    conn = connect_db()

    conn.execute("""
    UPDATE users
    SET password=?
    WHERE email=? OR contact=?
    """, (new_password, user_input, user_input))

    conn.commit()
    conn.close()

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)