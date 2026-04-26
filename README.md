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

**⚙️ Key Design Decisions**

* Used stratified sampling to preserve fraud ratio
* Saved datasets for reproducibility
* Modularized ingestion logic into reusable component

**Day 3 — Data Transformation Pipeline**
* Implemented data transformation component
* Applied scaling to transaction amount feature
* Built reusable preprocessing pipeline
* Saved preprocessor object for inference consistency
* Integrated transformation into training pipeline

**⚙️ Key Decisions**

* Only scaled Amount (other features already normalized via PCA)
* Saved preprocessing pipeline to ensure consistency across training and inference

**Day 4 — Model Training & Evaluation**

* Implemented model training pipeline
* Trained Logistic Regression and Random Forest models
* Used class balancing to handle imbalanced dataset
* Evaluated models using ROC-AUC metric
* Logged experiments using MLflow
* Selected best-performing model

**📊 Metrics Used**

* ROC-AUC (primary metric for imbalanced classification)

**⚙️ Performance Optimization**

* Enabled parallel processing using n_jobs=-1 in Random Forest
* Reduced training time significantly

**Day 5 — Prediction Pipeline & Risk Scoring**

* Built prediction pipeline for inference
* Loaded trained model and preprocessor
* Implemented probability-based predictions
* Added fraud risk classification (LOW / MEDIUM / HIGH)
* Performed threshold tuning using F1-score
* Converted model output into actionable decision system

**🔥 Key Features**

* Probability-based fraud detection
* Custom decision threshold
* Risk scoring system for interpretability