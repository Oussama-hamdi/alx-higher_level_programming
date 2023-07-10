#!/usr/bin/python3
"""
    This module provides a function
    for checking if the object isInstance of class"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class

        Args:
            obj: The object to check
            a_class: The class to match

        Returns: True if isInstance else False"""
    if (type(obj) == a_class):
        return True
    return False
