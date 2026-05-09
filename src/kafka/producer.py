from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC = "fraud-transactions"


def generate_transaction():
    return {
        "Time": random.randint(0, 100000),
        "V1": random.uniform(-2, 2),
        "V2": random.uniform(-2, 2),
        "V3": random.uniform(-2, 2),
        "V4": random.uniform(-2, 2),
        "V5": random.uniform(-2, 2),
        "V6": random.uniform(-2, 2),
        "V7": random.uniform(-2, 2),
        "V8": random.uniform(-2, 2),
        "V9": random.uniform(-2, 2),
        "V10": random.uniform(-2, 2),
        "V11": random.uniform(-2, 2),
        "V12": random.uniform(-2, 2),
        "V13": random.uniform(-2, 2),
        "V14": random.uniform(-2, 2),
        "V15": random.uniform(-2, 2),
        "V16": random.uniform(-2, 2),
        "V17": random.uniform(-2, 2),
        "V18": random.uniform(-2, 2),
        "V19": random.uniform(-2, 2),
        "V20": random.uniform(-2, 2),
        "V21": random.uniform(-2, 2),
        "V22": random.uniform(-2, 2),
        "V23": random.uniform(-2, 2),
        "V24": random.uniform(-2, 2),
        "V25": random.uniform(-2, 2),
        "V26": random.uniform(-2, 2),
        "V27": random.uniform(-2, 2),
        "V28": random.uniform(-2, 2),
        "Amount": random.uniform(1, 500)
    }


if __name__ == "__main__":
    while True:
        transaction = generate_transaction()
        producer.send(TOPIC, transaction)
        print("Sent:", transaction)
        time.sleep(1)