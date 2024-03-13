from bson import json_util
from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

connect(db="hw8", host="mongodb://localhost:27017")
uri = "mongodb+srv://userweb20:7654321@cluster0.mz2ef9x.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
db = client.web20

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=15))
    quote = StringField()
    meta = {"collection": "quotes"}

    def to_json(self, *args, **kwargs):
        data = self.to_mongo(*args, **kwargs)
        data["author"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)