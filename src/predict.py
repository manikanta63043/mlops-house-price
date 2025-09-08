import pickle
import pandas as pd

# Load model
with open("model/house_price.pkl", "rb") as f:
    model = pickle.load(f)

# Create a sample input with the SAME features used in training
sample = {
    "age": [50],
    "bmi": [25.3],
    "bp": [80],
    "s1": [150],
    "s2": [85],
    "s3": [45],
    "s4": [4.2],
    "s5": [5.6],
    "s6": [90]
}

df = pd.DataFrame(sample)

# Run prediction
prediction = model.predict(df)
print("✅ Prediction:", prediction)

