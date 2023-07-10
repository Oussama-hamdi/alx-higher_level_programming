#!/usr/bin/python3
"""This module provides a function for checking isInstance
    or inherited of a specific class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a given class

        Args:
            obj: The object to check
            a_class: The class to match
        Returns: True if isInstance else False
        """
    if isinstance(obj, a_class):
        return True
    return False
