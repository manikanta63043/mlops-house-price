import os
import pickle
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

# 1. Load dataset (here: diabetes dataset, you can replace with your house price data)
data = load_diabetes(as_frame=True)
X = data.data
y = data.target

# 2. Train model
model = LinearRegression()
model.fit(X, y)

# 3. Ensure model directory exists
os.makedirs("model", exist_ok=True)

# 4. Save trained model
with open("model/house_price.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model/house_price.pkl")
print("🧾 Trained on features:", list(X.columns))

