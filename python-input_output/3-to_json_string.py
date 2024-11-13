#!/usr/bin/python3
"""JSON function"""
import json


def to_json_string(my_obj):
    """function that return the JSON representation of a string object"""
    return json.dumps(my_obj)
