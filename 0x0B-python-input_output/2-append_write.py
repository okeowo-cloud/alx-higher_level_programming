#!/usr/bin/python3
"""2-append_write Module"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    :param filename: name of file to append characters
    :param text: the text to append to file

    :return: the number of characters appended

    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
