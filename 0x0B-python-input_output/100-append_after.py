#!/usr/bin/python3
"""100-append_after Module"""


def append_after(filename="", search_string="", new_string=""):
    """
    function inserts a line of text to a file, after each
    line containing a specific string

    :param filename: name of file to read or write
    :param search_string: string to look up
    :param new_string: string to append
    :return: void
    """
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as file:
        file.write(text)
