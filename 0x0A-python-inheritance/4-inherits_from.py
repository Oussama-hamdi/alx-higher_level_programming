#!/usr/bin/python3
"""This module provides a function for checking
    if an object is an inherited of a specific class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a given class
    Args:
        obj: The object to check
        a_class: The class to match
    Returns: True if obj is an inherited instance of a_class else False"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
