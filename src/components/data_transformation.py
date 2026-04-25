import os
import pandas as pd
import pickle

from sklearn.preprocessing import StandardScaler

class DataTransformation:
    def __init__(self):
        self.preprocessor_path = "artifacts/preprocessor.pkl"

    def initiate_data_transformation(self, train_path, test_path):
        print("Starting Data Transformation")

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        target_column = "Class"

        #Split features and target
        X_train = train_df.drop(columns=[target_column])
        y_train = train_df[target_column]
        X_test = test_df.drop(columns=[target_column])
        y_test = test_df[target_column]

        scaler = StandardScaler()
        X_train["Amount"] = scaler.fit_transform(X_train[["Amount"]])
        X_test["Amount"] = scaler.transform(X_test[["Amount"]])

        os.makedirs("artifacts", exist_ok=True)
        with open(self.preprocessor_path, "wb") as f:
            pickle.dump(scaler, f)

        print("Data Transformation Completed")
        return X_train, X_test, y_train, y_test