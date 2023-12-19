#!/usr/bin/env python3
"""defines a function
top_students"""


def top_students(mongo_collection):
    """takes a pymongo object and returns
    avg score for all students"""
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    top_students = list(mongo_collection.aggregate(pipeline))
    return top_students
