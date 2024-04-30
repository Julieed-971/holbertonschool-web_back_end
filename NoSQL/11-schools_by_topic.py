#!/usr/bin/env python3
"""Returns the list of school with specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with specific topic"""
    return mongo_collection.find({"topics": topic})
