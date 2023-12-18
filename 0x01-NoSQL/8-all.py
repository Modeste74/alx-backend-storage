#!/usr/bin/env python3
"""defines a function list_all"""
import pymongo


def list_all(mongo_collection):
    """takes in an object and list all
    documents in the collection inside it"""
    documents = list(mongo_collection.find({}))
    if mongo_collection is None:
       return []
    return documents
