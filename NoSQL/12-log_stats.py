#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Counts the total number of documents in the nginx_collection
    logs_count = nginx_collection.count_documents({})
    print("{} logs".format(logs_count))

    # Print the count of ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # methods in documents in logs
    print("Methods:")
    print("\tmethod GET: {}".format(nginx_collection.count_documents(
        {"method": "GET"})))
    print("\tmethod POST: {}".format(nginx_collection.count_documents(
        {"method": "POST"})))
    print("\tmethod PUT: {}".format(nginx_collection.count_documents(
        {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(nginx_collection.count_documents(
        {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(nginx_collection.count_documents(
        {"method": "DELETE"})))

    # Print the number of documents with method=GET and path=/status
    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))
