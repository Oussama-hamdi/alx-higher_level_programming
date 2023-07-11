#!/usr/bin/python3
"""This module provides a function to write a Python object
    to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using JSON"""
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
