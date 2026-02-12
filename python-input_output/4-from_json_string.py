#!/usr/bin/python3
"""
This module defines a function that returns a Python object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.
    """
    return json.loads(my_str)
