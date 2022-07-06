#!/usr/bin/python3
"""9-rectangle Module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle
        :param width: The width of the new Rectangle
        :param height: The height of the new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        String representation of a Rectangle
        :return: String representing a Rectangle
        """
        string = "[{}]".format(self.__class__.__name__)
        string += " {}/{}".format(self.__width, self.__height)
        return string

    def area(self):
        """
        Returns the area of a Rectangle
        :return: area of rectangle
        """
        return self.__width * self.__height
