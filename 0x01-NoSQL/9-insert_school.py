#!/usr/bin/env python3
"""defines a function insert_school"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """take an object, inserts the kwargs passed as
    a document"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
