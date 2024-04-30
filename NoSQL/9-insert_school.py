#!/usr/bin/env python3
"""Insert a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection and return the new _id"""
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
