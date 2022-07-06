#!/usr/bin/python3
"""2-is_same_class Module"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.
    :param obj: The object to check
    :param a_class: The class to match the type of obj to.
    :return: True, if obj is exactly an instance of a_class.
    """
    return type(obj) == a_class
