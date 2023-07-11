#!/usr/bin/python3
"""This module provides a function for appending text to a file"""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
