#!/usr/bin/python3
"""Module describes the real representation of a Rectangle
"""


class Rectangle:
    """ Rectangle class defines the representation of a rectangle
    :cvar number_of_instances - count the number of rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        Args:
            width(int): the width of the rectangle default to 0
            height(int): the height of the rectangle default to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns the area of the rectangle defined by the width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """
        :return the perimeter of the rectangle defined by 2 * (width + height)
        :return 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Defines the string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Defines the representation for rectangle instantiation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a custom message when a rectangle object is deleted
        decrements the number of instances of rectangle
        """
        if Rectangle.number_of_instances == 0:
            return
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
