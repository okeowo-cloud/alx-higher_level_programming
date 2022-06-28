#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """text_indentation docstring
    function adds 2 new lines after each of these characters: `.`, `?` and `:`

    :param text(str): is the text to be indented

    :return: void
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    arr = text.split(" ", -1)
    arr = [x for x in arr if x != ""]
    i = -1
    for item in arr:
        i += 1
        for k in range(0, len(item), 1):
            if item[k] == "\\":
                print(item[k: k+2], end="")
                k += 1
            print(item[k], end="")
            if item[k] == "." or \
                    item[k] == ":" or \
                    item[k] == "?":
                print("\n\n", end="")
        if arr[i].endswith("?") or \
                arr[i].endswith(":") or \
                arr[i].endswith("."):
            print("", end="")
        else:
            if i != len(arr) - 1 and \
                    not item.endswith("\n") and \
                    arr[i + 1] != "\n":
                print(" ", end="")
