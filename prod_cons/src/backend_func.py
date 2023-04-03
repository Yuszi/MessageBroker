from confluent_kafka import Consumer
from confluent_kafka import Producer
import logging

"""
    Zwischenserver für die Verwaltung von der versendeten Nachricht an die richtige Kategorie.
    Hierbei dient dieser sowohl als Consumer, als auch als Prouducer.
"""

# Verbindung zu Kafka als Consumer 
logging.info('Connecting to Kafka as Consumer')
zsConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})

# Verbindung zu Kafka als Producer
logging.info('Connecting as Producer')
p = Producer({'bootstrap.servers': 'localhost:9092'})

# Subscribtion an die Kategorie, damit dieser die Nachricht empfangen kann.
zsConsumer.subscribe(['zs'])
logging.info('Subscribed to Kafka as Zwischenspeicher to handle message')

def prod_send(msg):
    # Verwaltung der Nachicht 
    msg = msg.value().decode('utf-8')
    _msg = msg.lower().split(' ')
    topic = ""
    logging.info('Sending message as Producer to the specific topic after filtering')

    # Nachricht muss diese Wörter beinhalten, sonst Exception

    if any('sw' or 'software' in _msg for text in _msg): 
        topic = 'sw'
    
    if any('hw' or 'hardware' in _msg for text in _msg):
        topic = 'hw'

    
    p.produce(topic, msg)
    print(_msg)
    print(topic , " " , msg)
    topic = ""


# Einrichtung des laufenden "Servers"
while True: 
    # Empfange alle Nachrichten die vor 1 Sekunde hochgeladen wurde
    logging.info('Received Zwischenspeicher messages')
    msg = zsConsumer.poll(1.0)

    # Einfache Überprüfung der Nachricht
    if msg is None: 
        continue
    if msg.error():
        logging.fatal('Fehler auf der Seite vom Consumer')
        continue
    else: 
        logging.info('Got Message: {}'.format(msg.value().decode('utf-8')))
        prod_send(msg=msg)
        p.flush()



    
#zsConsumer.close()
