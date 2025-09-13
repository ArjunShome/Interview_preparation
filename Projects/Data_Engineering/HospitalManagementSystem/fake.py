from faker import Faker
import random
import uuid
import time
from datetime import datetime
from log import logger

class FakeData:
    def __init__(self, ceiling_freq, floor_freq):
        self.ceiling = ceiling_freq
        self.floor = floor_freq


    def fake_data(self):
        """_summary_
            Create fake data for one patient registry
        Returns:
            _type_: _description_
        """
        fake = Faker()
        current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        patient_id = str(uuid.uuid4())
        event_data = {
            "patient_id": patient_id,
            "patient_name": fake.name(),
            "patient_address": fake.address(),
            "registration_date": current_date_time,
        }
        logger.info(f"New Fake Data Generated: {patient_id}: {event_data}")
        return patient_id, event_data


    def generate_fake_data_at_interval(self):
        while True:
            interval = random.uniform(self.ceiling, self.floor)
            time.sleep(interval)
            # Call the function to generate the data and yield 
            patient_id, event = self.fake_data()
            yield patient_id, event