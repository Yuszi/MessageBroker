from confluent_kafka import Consumer

hwConsumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test-consumer-group',
})
hwConsumer.subscribe(['hw'])
""""
def getHardwareConsumer():
    while True:
        msg = hwConsumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer Error")
            continue

        print('Got Message: {}'.format(msg.value().decode('utf-8')))

    hwConsumer.close()
"""
while True:
    msg = hwConsumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer Error")
        continue

    print('Got Message: {}'.format(msg.value().decode('utf-8')))

hwConsumer.close()