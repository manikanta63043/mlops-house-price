import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load dataset
data = load_diabetes(as_frame=True)
X = data.data
y = data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
os.makedirs("../model", exist_ok=True)
with open("../model/house_price.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved at ../model/house_price.pkl")
