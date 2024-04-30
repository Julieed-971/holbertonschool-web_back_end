#!/usr/bin/env python3
"""
Lists all documents in a collection
"""

def list_all(mongo_collection):
    """Lists all documents in a collection"""

    # check if the collection is empty
    if mongo_collection.count_documents({}) == 0:
        print([])

    # if not empty, list and return all documents in collection
    return mongo_collection.find()
