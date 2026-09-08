import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

DATA_FILE = "../data/sample_production_data.csv"
MODEL_FILE = "anomaly_model.joblib"

df = pd.read_csv(DATA_FILE)

features = ["production_rate", "sensor_events"]
X = df[features].fillna(0)

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)
model.fit(X)

joblib.dump(model, MODEL_FILE)
print("Model saved to", MODEL_FILE)
