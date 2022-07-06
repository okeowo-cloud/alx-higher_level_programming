#!/usr/bin/python3
"""7-base_geometry Module"""


class BaseGeometry:
    """Defines the representation of BaseGeometry"""

    def area(self):
        """method raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method validate value
        :param name: a name string
        :param value: an integer greater than 0
        :return: void
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
