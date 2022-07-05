#!/usr/bin/python3
"""6-load_from_json_file Module"""
import json


def load_from_json_file(filename):
    """
    function creates an Object from a JSON file

    :param filename: name of file
    :return: returns Object representation of JSON
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
