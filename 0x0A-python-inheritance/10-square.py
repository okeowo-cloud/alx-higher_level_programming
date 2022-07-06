#!/usr/bin/python3
"""10-square Module"""

Rectangle = __import__("9-rectangle").Rectangle


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
