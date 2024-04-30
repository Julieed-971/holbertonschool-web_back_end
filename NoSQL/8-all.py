#!/usr/bin/env python3
"""
Lists all documents in a collection
"""

def list_all(mongo_collection):
    """Lists all documents in a collection"""

    # if not empty, list and return all documents in collection
    return mongo_collection.find()
