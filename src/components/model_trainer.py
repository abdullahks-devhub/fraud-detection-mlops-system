import os
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

import mlflow
import mlflow.sklearn



class ModelTrainer:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"

    def initiate_model_training(self, X_train, X_test, y_train, y_test):
        print("Starting Model Training")

        models = {
            "Logistic Regression": LogisticRegression(
                max_iter=2000,
                class_weight="balanced"
            ),
            "Random Forest": RandomForestClassifier(
                n_estimators=100,
                class_weight="balanced",
                n_jobs=-1
            )
        }

        best_model = None
        best_score = -1
        best_model_name = ""

        mlflow.set_experiment("Fraud-detection")

        for name, model in models.items():
            with mlflow.start_run(run_name=name):
                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)
                y_prob = model.predict_proba(X_test)

                roc_auc = roc_auc_score(y_test, y_prob[:, 1])

                print(f"{name} ROC AUC score: {roc_auc}")

                mlflow.log_metric("roc_auc", roc_auc)
                mlflow.sklearn.log_model(model, name)

                if roc_auc > best_score:
                    best_score = roc_auc
                    best_model_name = name
                    best_model = model

        os.makedirs("artifacts", exist_ok=True)

        with open(self.model_path, "wb") as f:
            pickle.dump(best_model, f)

        print(f"Best model: {best_model_name} with ROC AUC score: {best_score}")

        return self.model_path