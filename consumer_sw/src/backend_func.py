from confluent_kafka import Consumer
import logging
swConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})
swConsumer.subscribe(['sw'])

while True:
    logging.info('Software Consumer booted')
    msg = swConsumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer Error")
        continue

    print('Got Message: {}'.format(msg.value().decode('utf-8')))

swConsumer.close()