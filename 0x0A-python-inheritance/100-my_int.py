#!/usr/bin/python3
"""100-my_int Module"""


class MyInt(int):
    """Representation of an int"""
    
    def __eq__(self, other):
        """
        Overides the equal method of python built-in int
        :param other: another value of int
        :return: boolean
        """
        return self.real != other

    def __ne__(self, other):
        """
        Overrides the equal method of python built-in int
        :param other: another value of int
        :return: boolean
        """
        return self.real == other
