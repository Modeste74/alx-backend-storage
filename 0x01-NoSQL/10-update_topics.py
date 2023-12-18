#!/usr/bin/env python3
"""defines a function update_topics"""
# import pymongo


def update_topics(mongo_collection, name, topics):
    """accepts an objects, a name and list of topics
    . It changes the list of topics based on the name"""
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
