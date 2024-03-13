from bson import json_util
from mongoengine import connect, Document, StringField, ReferenceField, ListField, CASCADE

connect(db="hw20", host="mongodb+srv://userweb20:7654321@cluster0.mz2ef9x.mongodb.net/")
# host="mongodb://localhost:27017"

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
        data["authors"] = self.author.fullname
        return json_util.dumps(data, ensure_ascii=False)