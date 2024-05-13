from kafka import KafkaConsumer

# Configuration du consommateur Kafka
consumer = KafkaConsumer('tweets', 
                        bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='latest',
                        enable_auto_commit=True,
                        auto_commit_interval_ms=5000,
                        fetch_max_bytes=128,
                        max_poll_records=100,)

# Lecture et affichage des messages du topic
for message in consumer:
    print(f"Message: {message.value}")
