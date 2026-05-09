import os
import pickle
import pandas as pd

class PredictionPipeline:
    def __init__(self):
        # Use absolute path based on the file location to ensure robust execution
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.model_path = os.path.join(base_dir, "artifacts", "model.pkl")
        self.preprocessor_path = os.path.join(base_dir, "artifacts", "preprocessor.pkl")
        
        # Load model and preprocessor into memory once during initialization
        self.model = self._load_model()
        self.preprocessor = self._load_preprocessor()

    def _load_model(self):
        with open(self.model_path, "rb") as f:
            return pickle.load(f)

    def _load_preprocessor(self):
        with open(self.preprocessor_path, "rb") as f:
            return pickle.load(f)

    def predict(self, data: dict):
        df = pd.DataFrame([data])

        # Use pre-loaded preprocessor and model
        df["Amount"] = self.preprocessor.transform(df[["Amount"]])
        prob = self.model.predict_proba(df)[:, 1][0]
        
        return prob

    def get_risk(self, prob):
        if prob < 0.3:
            return "LOW 🟢"
        elif prob < 0.7:
            return "MEDIUM 🟡"
        else:
            return "HIGH 🔴"

    def get_confidence(self, prob):
        if prob < 0.1 or prob > 0.9:
            return "HIGH CONFIDENCE"
        elif prob < 0.3 or prob > 0.7:
            return "MEDIUM CONFIDENCE"
        else:
            return "LOW CONFIDENCE"

    def predict_with_risk(self, data: dict):
        prob = self.predict(data)
        risk = self.get_risk(prob)

        threshold = 0.265306
        prediction = 1 if prob > threshold else 0
        confidence = self.get_confidence(prob)

        return{
            "fraud_probability": float(prob),
            "prediction": int(prediction),
            "risk_level": risk,
            "confidence": confidence
        }