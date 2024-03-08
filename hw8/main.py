from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://userweb20:7654321@cluster0.mz2ef9x.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

db = client.autors

try:
    db.tag.insert_many(
        [
            {
                "name": "Boris",
                "age": 12,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Murzik",
                "age": 1,
                "features": ["ходить в лоток", "дає себе гладити", "чорний"],
            },
        ]
    )
except Exception as e:
    print(e)