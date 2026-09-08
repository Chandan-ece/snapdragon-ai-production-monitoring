import joblib
import numpy as np

MODEL_FILE = "anomaly_model.joblib"

model = joblib.load(MODEL_FILE)

def detect_anomaly(production_rate, sensor_events):
    X = np.array([[production_rate, sensor_events]])
    prediction = model.predict(X)[0]
    return "ANOMALY" if prediction == -1 else "NORMAL"

if __name__ == "__main__":
    print(detect_anomaly(10, 10))
