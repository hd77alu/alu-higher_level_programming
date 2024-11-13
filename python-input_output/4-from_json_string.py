#!/usr/bin/python3
"""JSON function"""
import json


def from_json_string(my_str):
    """function that return the JSON representation of a string object"""
    return json.loads(my_str)
