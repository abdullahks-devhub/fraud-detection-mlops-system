import os
import pickle
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"
        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def load_model(self):
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)
        return model

    def load_preprocessor(self):
        with open(self.preprocessor_path, "rb") as f:
            preprocessor = pickle.load(f)
        return preprocessor

    def predict(self, data: dict):
        model = self.load_model()
        preprocessor = self.load_preprocessor()

        df = pd.DataFrame([data])

        df["Amount"] = preprocessor.transform(df[["Amount"]])

        prob = model.predict_proba(df)[:, 1][0]
        return prob

    def get_risk(self, prob):
        if prob < 0.3:
            return "LOW 🟢"
        elif prob < 0.7:
            return "MEDIUM 🟡"
        else:
            return "HIGH 🔴"

    def predict_with_risk(self, data: dict):
        prob = self.predict(data)
        risk = self.get_risk(prob)

        threshold = 0.265306
        prediction = 1 if prob > threshold else 0

        return{
            "fraud_probability": float(prob),
            "prediction": int(prediction),
            "risk_level": risk
        }