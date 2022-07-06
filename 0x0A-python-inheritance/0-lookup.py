#!/usr/bin/python3
"""0-lookup Module"""


def lookup(obj):
    """
    function return a list of available attributes and methods of an object:
    :param obj: object to determine methods and attributes
    :return: list of all attributes and methods of object
    """
    return dir(obj)
