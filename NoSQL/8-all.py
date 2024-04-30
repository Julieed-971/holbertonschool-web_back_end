#!/usr/bin/env python3
"""
Lists all documents in a collection
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    # connect to MongoDB
    MongoClient(host="localhost", port=27017)

    # check if the collection is empty
    if mongo_collection.count_documents({}) == 0:
        print([])

    # if not empty, list and return all documents in collection
    documents = mongo_collection.find()
    return documents
