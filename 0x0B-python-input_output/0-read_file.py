#!/usr/bin/python3
"""Module 0-read_file"""


def read_file(filename=""):
    """functio read a file and prints it

    :param filename: path to file to be read
    :return: Always void.

    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
