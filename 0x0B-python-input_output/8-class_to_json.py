#!/usr/bin/python3
"""This module provides a function to return the dictionary
    description of a class object"""


def class_to_json(obj):
    """Return the dictionary description of a class object"""
    return obj.__dict__
