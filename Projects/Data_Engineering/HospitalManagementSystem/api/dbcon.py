from pymongo import MongoClient
from urllib.parse import quote_plus

MONGO_USERNAME = quote_plus("arjun")
MONGO_PASSWORD = quote_plus("mongo@1234")
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "hospital_management_system"

# Create Mongo Client
client = MongoClient(
    f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
)
db = client[MONGO_DB]