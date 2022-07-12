#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the representation of a square object based on rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square based on a Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a Square object"""
        s = "[{}] ({})".format(self.__class__.__name__, self.id)
        return s + " {}/{} - {}".format(self.x, self.y, self.width)

    @property
    def size(self):
        """getter for the size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size of a square
        :param value: new size of square
        :return: void
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method assigns attributes to method arguments
        :param args: variable number of method arguments
        :param kwargs: key word arguments, key/value pair arguments
        :return: void
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for k, v in kwargs.items():
                    if k == "id":
                        if v is None:
                            self.__init__(
                                    self.width, self.width, self.x, self.y)
                        else:
                            self.id = v
                    elif k == "size":
                        self.width = v
                        self.height = v
                    elif k == "x":
                        self.x = v
                    elif k == "y":
                        self.y = v

    def to_dictionary(self):
        """dictionary representation of a square object"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
