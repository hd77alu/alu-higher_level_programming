#!/usr/bin/python3
"""JSON file-reading function."""
import json


def load_from_json_file(filename):
    """function that Creates an object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
