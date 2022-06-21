#!/usr/bin/python3
"""Square Docstring

Module defines a Square with size

"""


class Square:
    """ Represent a square """

    def __init__(self, size=0):
        """ Initialize a new square.

        Args:
        size(int): The size of the new square.

        """
        self.__size = size

    @property
    def size(self):
        """ return the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area function docstring.

        Returns:
        int: The return value value representing the area of square

        """
        return (self.__size * self.__size)
