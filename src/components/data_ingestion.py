import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        self.raw_data_path = "artifacts/raw.csv"
        self.train_data_path = "artifacts/train.csv"
        self.test_data_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):
        print("Starting Data Ingestion")

        df = pd.read_csv(self.raw_data_path)

        df = df.dropna()

        print(f"Dataset shape after cleaning: {df.shape}")
        train_df, test_df = train_test_split(
            df,
            test_size=0.2,
            random_state=42,
            stratify=df["Class"]
        )

        os.makedirs("artifacts", exist_ok=True)
        train_df.to_csv(self.train_data_path, index=False)
        test_df.to_csv(self.test_data_path, index=False)

        print("Data Ingestion Completed")
        print(f"Train shape: {train_df.shape}")
        print(f"Test shape: {test_df.shape}")

        return self.train_data_path, self.test_data_path