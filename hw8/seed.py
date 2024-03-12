import json

from mongoengine.errors import NotUniqueError

from models import Author, Quote
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# uri = "mongodb+srv://userweb20:7654321@cluster0.mz2ef9x.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection

# db = client.hw8
if __name__ == '__main__':
    uri = "mongodb+srv://userweb20:7654321@cluster0.mz2ef9x.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

    db = client.hw8
    with open('authors.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except NotUniqueError:
                print(f"Автор вже існує {el.get('fullname')}")

    with open('qoutes.json', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            author, *_ = Author.objects(fullname=el.get('author'))
            quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
            quote.save()
            