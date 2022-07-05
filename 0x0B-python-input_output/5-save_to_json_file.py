#!/usr/bin/python3
"""5-save_to_json_file Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    function writes an object to a text file using a JSON representation

    :param my_obj: object to write to text file as JSON
    :param filename: name of file

    :return: void
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
