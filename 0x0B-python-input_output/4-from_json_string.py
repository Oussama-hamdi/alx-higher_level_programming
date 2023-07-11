#!/usr/bin/python3
"""This module provides a function to convert a JSON
    representation into an object"""

import json


def from_json_string(my_str):
    """Convert a JSON representation into an object"""
    return json.loads(my_str)
