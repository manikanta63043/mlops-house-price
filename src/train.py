import pickle
import os

# your training code here
# model = ...

# Ensure model directory exists
os.makedirs("model", exist_ok=True)

# Save the model
with open("model/house_price.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved at model/house_price.pkl")
