#!/usr/bin/python3
"""Module describes the real representation of a Rectangle
"""


class Rectangle:
    """ Rectangle class defines the representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width(int): the width of the rectangle default to 0
            height(int): the height of the rectangle default to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve the width of the rectangle
        :return the width of the rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width of the rectangle
        :param value: is the value of the width to set
        :return: void
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieve the height of the rectangle
        :return: the height of the rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height of the rectangle
        :param value: the value of the height to be set
        :return: void
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle defined by the
        width multiplied by height"""
        return (self.__width * self.__height)

    def perimeter(self):
        """
        :return the perimeter of the rectangle
        defined by (width + height) * 2

        :return 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)
