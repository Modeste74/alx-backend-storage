#!/usr/bin/env python3
"""defines a function log_stats"""
from pymongo import MongoClient


def log_stats():
    """provides some stats about Nginx
    logs stored in MongoDB"""
    client = MongoClient("mongodb://localhost:27017")
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_chk = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_chk} status check")


if __name__ == "__main__":
    log_stats()
