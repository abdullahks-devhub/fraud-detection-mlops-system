from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    print("Starting Training Pipeline")
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformer = DataTransformation()
    X_train, X_test, y_train, y_test = transformer.initiate_data_transformation(
        train_path, test_path
    )
    print("Pipeline executed successfully")