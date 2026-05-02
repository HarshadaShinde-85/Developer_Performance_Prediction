import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv("developer_data.csv")

# Convert ALL text columns automatically using factorization
for column in data.columns:
    if data[column].dtype == "object":
        data[column], _ = pd.factorize(data[column])

# Separate features and target
X = data.drop("Performance", axis=1)
y = data["Performance"]

# Train model
model = LogisticRegression(max_iter=10000)
model.fit(X, y)

# Save trained model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained and saved successfully!")