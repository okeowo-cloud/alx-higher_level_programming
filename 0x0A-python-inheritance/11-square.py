#!/usr/bin/python3
"""11-square Module"""


Rectangle = __import__("8-rectangle").Rectangle


class Square(Rectangle):
    """Defines the representation of a Square"""

    def __init__(self, size):
        """
        Initialize a new Square
        :param size: the size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns the area of a Square
        :return: area of Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        The string representation of a Square
        :return: string representation of square
        """
        string = "[{}]".format(self.__class__.__name__)
        string += " {}/{}".format(self.__size, self.__size)
        return string
