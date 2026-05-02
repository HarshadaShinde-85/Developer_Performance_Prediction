# 📊 Developer Performance Prediction System
🚀 Project Overview

The Developer Performance Prediction System is a Machine Learning–based web application that predicts developer performance (Low, Medium, High) using productivity-related metrics such as coding hours, errors, stress level, commits, and complexity.

The system includes:

Secure login & registration
OTP-based password reset (Email + SMS)
Machine learning prediction 
Interactive dashboard
SQLite database integration
Flask web interface

This project demonstrates the integration of Machine Learning + Web Development + Authentication System in a real-world productivity analytics solution.

# 🎯 Key Features

✅ Developer registration with profile details
✅ Secure login authentication
✅ Forgot password with OTP verification
✅ Email notification on registration
✅ SMS notification support (Twilio)
✅ Performance prediction using ML model
✅ Clean responsive UI with HTML + CSS
✅ SQLite database integration
✅ Flask backend architecture

# 🧠 Machine Learning Model

The system uses:

Logistic Regression classifier
Feature scaling with StandardScaler
Encoded categorical inputs
Performance prediction categories:
Output	Meaning
0	Low Performance
1	Medium Performance
2	High Performance

# 📂 Project Structure
Developer-Performance-Prediction/
│
├── app.py
├── train_model.py
├── model.pkl
├── users.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── result.html
│   ├── forgot_password.html
│   ├── verify_otp.html
│   └── new_password.html
│
├── static/
│   └── style.css
│
├── developer_data.csv
├── README.md

# ⚙️ Technologies Used
Frontend:
HTML5
CSS3

Backend:
Python
Flask
SQLite

Machine Learning:
Scikit-learn
Pandas
NumPy

Authentication Services:
Gmail SMTP
Twilio SMS API

# 🛠️ Installation Steps

Follow these steps to run the project locally:

1️⃣ Clone Repository
git clone https://github.com/yourusername/developer-performance-prediction.git
cd developer-performance-prediction
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install flask pandas numpy scikit-learn twilio
4️⃣ Train Model (if needed)
python train_model.py

This creates:

model.pkl

5️⃣ Run Application
python app.py

Open browser:

http://127.0.0.1:5000

# 🔐 Authentication Workflow

The system supports:

Registration confirmation email
SMS alerts on account creation
OTP verification for password reset
Secure session-based login/logout

# 📊 Input Features Used for Prediction

The model predicts performance using:

Hours Coding
Lines of Code
Bugs Found
Bugs Fixed
AI Usage Hours
Sleep Hours
Cognitive Load
Task Success Rate
Coffee Intake
Stress Level
Task Duration Hours
Commits
Errors
Complexity

# 📈 Prediction Output Example
Predicted Developer Performance: High Performance ✅

# 💡 Future Improvements

Planned enhancements:

Role-based admin dashboard
Performance analytics charts
Deployment on cloud (Render / AWS)
Real-time productivity tracking API

# 👩‍💻 Author

Harshada Shinde
Developer Performance Prediction System
