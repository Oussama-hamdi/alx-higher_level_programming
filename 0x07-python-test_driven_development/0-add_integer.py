#!/usr/bin/pyhton3
"""A function that adds two numbers"""


def add_integer(a, b=98):
    """Return the addition of a and b"""
    if type(a) not in [int, float] and type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    return int(a) + int(b)
