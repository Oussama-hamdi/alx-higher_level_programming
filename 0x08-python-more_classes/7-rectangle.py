#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """A class represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width (int): Width of the rectangle default = 0
            height (int): Height of the rectangle default =0
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
            raise ValueError("height must be >= 0")
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        self.__height = val

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of ther rectangle"""
        if not self.__width or not self.__height:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the rectangle with the (#) symbol"""
        if not self.__width or not self.__height:
            return ""
        symbol = str(self.print_symbol)
        new_str = ""
        for i in range(self.__height):
            new_str += symbol * self.__width
            if i + 1 < self.__height:
                new_str += "\n"
        return new_str

    def __repr__(self):
        """Return a string representaion of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the instance of the Rectangle and prints message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
