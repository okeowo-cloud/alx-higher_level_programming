#!/usr/bin/python3
"""3-say_my_name module"""


def say_my_name(first_name, last_name=""):
    """say_my_name function docstring
    function prints first_name and last_name

    :param first_name(string): first name
    :param last_name(string): last name

    :return: a formatted full name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
