from confluent_kafka import Producer, Consumer, KafkaException
from fake import FakeData
import json
from log import logger


TOPIC = "patient_registrations"

class KafkaProducer:
    PRODUCER_CONF = {
        "bootstrap.servers": "localhost:9092",
        "compression.type": "zstd",
        "linger.ms": "10000",
        "enable.idempotence": True,
        "acks": "all"
    }
    def __init__(self):
        self._producer = None

    def start(self):    
        if self._producer is None:
            self._producer = Producer(self.PRODUCER_CONF)

    def on_delivery(self, error, message):
        if error:
            logger.error(f"Delivery Failed With error {error}")
        else:
            logger.info(f"Delivery Successfull: TOPIC-{message.topic()}, PATIENT_ID-{message.key().decode()}")


    def run(self):
        self.start()
        logger.info("Kafka Producer Started.")
        try:
            source_data = FakeData(1, 10) # Faking data generation, waiting randomly for 1 to 10 seconds
            for patient_id, event in source_data.generate_fake_data_at_interval():
                self._producer.produce(
                    TOPIC,
                    key=patient_id,
                    value=json.dumps(event),
                    on_delivery=self.on_delivery
                )
                self._producer.poll(0)
        except KeyboardInterrupt:
            logger.info("Producer Stoped!!")
        finally:
            logger.info("Flushing..")
            self._producer.flush()
            logger.info("Flushed.")


class KafkaConsumer:
    CONSUMER_CONF = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "patient-consumer-group" + str(int(__import__("time").time())),
        "auto.offset.reset": "earliest"
    }
    def __init__(self):
        self._consumer = None

    def start(self):
        if self._consumer is None:
            self._consumer = Consumer(self.CONSUMER_CONF)
            self._consumer.subscribe([TOPIC])

    def run(self):
        self.start()
        try:
            self._consumer.list_topics(timeout=10)
            logger.info("Kafka Consumer Started... Waiting for message..")
            while True:
                # Poll for 1 second to receive the message
                msg = self._consumer.poll(1.0)
                if not msg:
                    logger.info("Waiting for message ... ")
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                
                # decode the message if there is a new message
                logger.info("Received 1 new Message.")
                patient_id = msg.key().decode('utf-8')
                event = json.loads(msg.value().decode('utf-8'))
                logger.info(f"Patient_id: {patient_id} Patient Details: {event}")

        except KeyboardInterrupt:
            logger.info("Consumer Stopped by the User")
        finally:
            self._consumer.close()

    