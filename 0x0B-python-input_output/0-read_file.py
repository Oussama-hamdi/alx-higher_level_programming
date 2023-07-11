#!/usr/bin/python3
"""This module provides a function for reading and printing the contents
    of a text file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and print it to stdout"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
