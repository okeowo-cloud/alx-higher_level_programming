#!/usr/bin/pthon3
"""8-rectangle Module"""


BaseGeometry = __import__("6-base_geometry").BaseGeometry


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
