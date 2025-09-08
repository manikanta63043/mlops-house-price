import pickle
import pandas as pd

# Load trained model
with open("../model/house_price.pkl", "rb") as f:
    model = pickle.load(f)

# Example input (replace with real values)
data = {
    "Rooms": [3],
    "Distance": [5.0],
    "Bathroom": [2],
    "Landsize": [150],
}

df = pd.DataFrame(data)

# Make prediction
prediction = model.predict(df)
print("🏠 Predicted House Price:", prediction[0])
