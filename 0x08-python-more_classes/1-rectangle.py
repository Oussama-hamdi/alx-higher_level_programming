#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """A class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width (int): Width of the rectangle default = 0
            height (int): Height of the rectangle default =0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter method"""
        if val < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        self.__width = val

    @property
    def height(self):
        """Getter method"""
        return self.__height

    @height.setter
    def height(self, val):
        """Setter method"""
        if val < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        self.__height = val
