from confluent_kafka import Consumer
import logging


"""
    Einrichtung des Software-Consumer-Servers.
"""

# Verbindung zu Kafka als Consumer 
logging.info('Connecting to Kafka as Consumer')
swConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})
# Subscribtion an die Kategorie, damit dieser die Nachricht empfangen kann.
swConsumer.subscribe(['sw'])
logging.info('Subscribing to Kafka as Hardware Consumer')

while True:
    # Empfange alle Nachrichten die vor 1 Sekunde hochgeladen wurde
    logging.info('Getting old messages from sw topic')
    msg = swConsumer.poll(1.0)

    # Einfache Überprüfung der Nachricht
    if msg is None:
        continue
    if msg.error():
        logging.fatal("Consumer Error")
        continue

    logging.info('Got Message: {}'.format(msg.value().decode('utf-8')))

#swConsumer.close()