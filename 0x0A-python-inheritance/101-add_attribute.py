#!/usr/bin/python3
"""101-add_attribute Module"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an Object if possible

    :param obj: The object to add an attribute to
    :param attr: The name of the attribute to add to obj
    :param value: The value of att

    :raise TypeError if the attribute cannot be add
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
