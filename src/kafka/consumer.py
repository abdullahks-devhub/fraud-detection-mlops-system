from kafka import KafkaConsumer
import json

from src.pipeline.prediction_pipeline import PredictionPipeline

consumer = KafkaConsumer(
    "fraud-transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

pipeline = PredictionPipeline()

print("Consumer started...")

for message in consumer:
    data = message.value

    result = pipeline.predict_with_risk(data)

    print("Transaction:", data)
    print("Prediction:", result)
    print("-" * 50)