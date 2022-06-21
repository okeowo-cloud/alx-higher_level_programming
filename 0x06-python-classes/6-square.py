#!/usr/bin/python3
"""Square Docstring

Module defines a Square with size

"""


class Square:
    """ Represent a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new square.

        Args:
        size(int): The size of the new square.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ return the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value of the position of the square """
        if (not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeEror("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area function docstring.

        Returns:
        int: The return value value representing the area of square

        """
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
