#!/usr/bin/python3
"""This module defines Base class"""


class Base:
    """Base class for the whole project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
