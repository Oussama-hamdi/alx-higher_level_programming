#!/usr/bin/python3
"""This module provides a function for looking up an object's attributes"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (dir(obj))
