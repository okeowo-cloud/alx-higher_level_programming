#!/usr/bin/python3
"""1-write_file Module"""


def write_file(filename="", text=""):
    """
    function writes a UTF8 text file

    :param filename: name of file to write
    :param text: the text to write
    :return: number of characters written

    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
