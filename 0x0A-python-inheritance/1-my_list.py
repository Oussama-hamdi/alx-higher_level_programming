#!/usr/bin/python3
"""This module defines a custom class MyList that inherits from list class"""


class MyList(list):
    """A custom list class that adds additional functionality"""

    def print_sorted(self):
        print(sorted(self))
