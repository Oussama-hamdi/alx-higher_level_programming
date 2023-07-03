#!/usr/bin/pyhton3
"""A function that adds two numbers"""


def add_integer(a, b=98):
    """
    Return the addition of a and b.
    
    Args:
        a (int or float): a number.
        b (int or float): a number.

    Returns:
        int: integer

    Raises:
        TypeError: If one of the parameters is a not a number
    
    """
    if type(a) not in [int, float] and type(b) not in [int, float]:
        raise TypeError("a must be an integer")
    return int(a) + int(b)
