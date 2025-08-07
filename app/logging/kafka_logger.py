import os
import json
from aiokafka import AIOKafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
KAFKA_TOPIC = os.getenv("KAFKA_LOG_TOPIC", "logtopic")

# Create producer globally
producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

async def start_kafka_producer():
    await producer.start()

async def stop_kafka_producer():
    await producer.stop()

async def log_event(event: dict):
    try:
        # Send message and wait for delivery confirmation
        result = await producer.send_and_wait(
            KAFKA_TOPIC, 
            json.dumps(event).encode("utf-8")
        )
        print(f"Kafka log delivered to {result.topic} [{result.partition}]")
    except Exception as e:
        print(f"Kafka log error: {e}")