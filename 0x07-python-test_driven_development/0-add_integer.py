#!/usr/bin/python3
"""0-add_integer Docstring
Module adds two integers and returns an integer
"""


def add_integer(a, b=98):
    """ function adds two integers

    if args are float they are casted to integer

    Args:
    :param a: might be an integer or float
    :param b: might be an integer or float

    :raise Exception: TypeError

    :return: is an integer

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
