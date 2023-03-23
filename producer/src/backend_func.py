from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def producerKafkaSend(topic: str, message: str) -> None:
    p.poll(0)
    p.produce(topic, message.encode('utf-8'))
    p.flush()