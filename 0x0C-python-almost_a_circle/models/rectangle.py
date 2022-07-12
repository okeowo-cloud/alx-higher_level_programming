#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Defines the representation of a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle

        :param width: width of the rectangle
        :param height: height of the rectangle
        :param x:
        :param y:

        :raises TypeError:if width, height, x, y is not an integer
        :raises ValueError: if width height, x, y is < or <= 0

        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width
        get the current value of width
        :return: current width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width
        set the value of width to the value param

        :param value: value to se width to

        :raises TypeError: if width is not an integer
        :raises ValueError: if width is not an integer

        :return: void
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height
        gets the current value of height
        :return : current value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height
        set the value of height to the value param

        :param value: value to set height to

        :raises TypeError: if height is not an integer
        :raises ValueError: if height is <= 0

        :return: void
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x
        get the current value of x
        :return: the current value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x
        set the value of x to the value param

        :param value: value to assign to x

        :raises TypeError if value is not an integer
        :raises ValueError if value is less than 0

        :return: void
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y
        :return: the current value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y
        assign the value param to y

        :param value: value to assign to y

        :raises TypeError if value is not an integer
        :raises ValueError if value is less than 0

        :return: void
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function returns area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Display a rectangle"""
        for a in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.width + self.x):
                if (j < self.x):
                    print(" ", end="")
                else:
                    print("#", end="")
            print("")

    def __str__(self):
        """string representation of a Rectangle"""
        s = "[{}] ({}) ".format(self.__class__.__name__, self.id)
        c = "{}/{} - {}/{}".format(self.x, self.y, self.width, self.height)
        return s + c

    def update(self, *args, **kwargs):
        """update method assigns an argument to each attribute
        :param args: is a variable number argument
        :param kwargs: key/value pair dict of attribute and argument
        :return: void
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """dictionary representation of a rectangle object"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
