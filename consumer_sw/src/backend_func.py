from confluent_kafka import Consumer
import logging

logging.info('Connecting to Kafka as Consumer')
swConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})
swConsumer.subscribe(['sw'])
logging.info('Subscribing to Kafka as Hardware Consumer')

while True:
    logging.info('Software Consumer booted')
    msg = swConsumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logging.fatal("Consumer Error")
        continue

    logging.error('Got Message: {}'.format(msg.value().decode('utf-8')))

swConsumer.close()