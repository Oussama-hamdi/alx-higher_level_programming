#!/usr/bin/python3
"""This module provides a function to convert an object (string)
    to its JSON representation"""

import json


def to_json_string(my_obj):
    """Convert an object (string) to its JSON representation"""
    return json.dumps(my_obj)
