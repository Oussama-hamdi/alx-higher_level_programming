#!/usr/bin/python3
"""This module defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):

        return self.width

    @size.setter
    def size(self, value):

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        if args:
            super().update(*args)
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
