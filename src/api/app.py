from fastapi import FastAPI
from src.pipeline.prediction_pipeline import PredictionPipeline
from pydantic import BaseModel

app = FastAPI(title="Fraud Detection API")

pipeline = PredictionPipeline()


class TransactionInput(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

class PredictionOutput(BaseModel):
    fraud_probability: float
    prediction: int
    risk_level: str
@app.get("/")
def home():
    return {"message": "Fraud Detection API is running 🚀"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: TransactionInput):
    result = pipeline.predict_with_risk(data.dict())
    return result

