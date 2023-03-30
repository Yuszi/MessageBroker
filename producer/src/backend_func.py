from confluent_kafka import Producer
"""
    Hier wird die Verbindung zu Kafka als Producer hergestellt und die geschriebene Nachricht
    vom Client versendet.
"""

# Verbindung zu Kafka wird hergestellt
p = Producer({'bootstrap.servers': 'localhost:9092'})

def producerKafkaSend(message: str) -> None:
    # Ließ die Nachrichten von vor 0 Sekunden (siehe Handbuch)
    p.poll(0)
    
    # Versende die Nachricht zu dem Zwischenspeicher, damit der Zwischenserver die Nachricht verwalten kann.
    p.produce('zs', message.encode('utf-8')) 
    p.flush()