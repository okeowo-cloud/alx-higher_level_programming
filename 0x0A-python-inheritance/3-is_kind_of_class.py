#!/usr/bin/python3
"""3-is_kind_of_class Module"""


def is_kind_of_class(obj, a_class):
    """
    determines if an object is an instance of, or if the
    object is an instance of a class that inherited from
    the specified class.
    :param obj: obj to check
    :param a_class: The class to match the type of obj to
    :return: True, if obj is an instance or inherits from a_class
    """
    return isinstance(obj, a_class)
