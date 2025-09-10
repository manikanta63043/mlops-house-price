import os
import pickle
import pandas as pd

def test_model_file_exists():
    """Check if trained model file exists"""
    assert os.path.exists("model/house_price.pkl")

def test_prediction_output():
    """Check if model can make a prediction"""
    with open("model/house_price.pkl", "rb") as f:
        model = pickle.load(f)

    # sample input - must match training features
    sample = {
        "age": [50],
        "sex": [1],
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
    prediction = model.predict(df)

    assert prediction is not None
    assert len(prediction) == 1
