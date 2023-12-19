#!/usr/bin/env python3
"""defines a function
schools_by_topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """takes a mongo object and topic
    by which schools are to be searched for"""
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
