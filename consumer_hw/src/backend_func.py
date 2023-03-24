from confluent_kafka import Consumer
import logging

logging.info('Connecting to Kafka as Consumer')
hwConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})
logging.info('Subscribing to Kafka as Hardware Consumer')
hwConsumer.subscribe(['hw'])

while True:
    logging.info('Getting old messages from hw topic')
    msg = hwConsumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        logging.fatal("Consumer Error")
        continue

    logging.info('Got Message: {}'.format(msg.value().decode('utf-8')))

hwConsumer.close()