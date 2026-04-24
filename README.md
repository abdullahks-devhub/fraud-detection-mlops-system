**Day 1 — Exploratory Data Analysis**
* Performed in-depth EDA on the credit card fraud dataset.
* Key Observations:
* Extreme class imbalance (~0.17% fraud cases)
* No missing values in dataset
* Features are PCA-transformed (V1–V28)
* Transaction amount is highly skewed
* Several features show correlation with fraud class
* Time feature can simulate real-time streaming

**Day 2 — Data Ingestion Pipeline**
* Implemented data ingestion component
* Loaded and cleaned dataset (removed corrupted rows)
* Performed stratified train-test split
* Saved train and test datasets as artifacts
* Created training pipeline entry point
⚙️ Key Design Decisions
* Used stratified sampling to preserve fraud ratio
* Saved datasets for reproducibility
* Modularized ingestion logic into reusable component