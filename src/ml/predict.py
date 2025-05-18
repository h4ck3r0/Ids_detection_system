
import joblib
import numpy as np

model = joblib.load("models/ids_model.pkl")
scaler = joblib.load("models/scaler.pkl")


def predict(features):
    features = np.array(features).reshape(1, -1)
    scaled = scaler.transform(features)
    return model.predict(scaled)[0]