from pymongo import MongoClient


MONGO_DETAILS = "mongodb://mongodb:27017"
client = MongoClient(MONGO_DETAILS)
db = client.Products
laptops_collection = db.Laptops


def get_laptops():
    return laptops_collection.find({})


def add_laptops(laptops):
    return laptops_collection.insert_many(laptops)
