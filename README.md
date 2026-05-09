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

**Day 6 — FastAPI Deployment**

* Built REST API using FastAPI
* Created /predict endpoint for fraud detection
* Implemented request validation using Pydantic
* Integrated prediction pipeline into API
* Enabled interactive API testing using Swagger UI

**🚀 Features**

* Real-time fraud prediction
* Structured input validation
* Risk-based decision output
* Interactive API documentation

**Day 7 — Dockerization**

* Containerized FastAPI application using Docker
* Created production-ready Dockerfile
* Added .dockerignore to optimize image size
* Enabled container-based deployment
* Integrated remote model loading (Hugging Face)

**🚀 Features**

* Portable ML API
* Environment-independent execution
* Ready for cloud deployment

**📅 Day 8 — Kafka Streaming Integration**

* Integrated Apache Kafka using Docker Compose
* Built producer-consumer streaming architecture
* Enabled real-time fraud prediction from transaction streams
* Implemented event-driven ML inference pipeline

**🚀 Technologies Added**

* Apache Kafka
* Zookeeper
* Docker Compose

**⚡ Real-Time Streaming Inference**

* Kafka consumer continuously listens for incoming transactions
* Producer simulates live transaction stream
* Fraud predictions generated in real time