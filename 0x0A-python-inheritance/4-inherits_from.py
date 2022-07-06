#!/usr/bin/python3
"""4-inherits_from Module"""


def inherits_from(obj, a_class):
    """
    function determines if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    :param obj: obj to check
    :param a_class: the class to match the type of the obj to
    :return: True, if obj inherits directly or indirectly from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
