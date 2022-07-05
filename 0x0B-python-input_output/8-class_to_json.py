#!/usr/bin/python3
"""8-class_to_json Module"""
import json


def class_to_json(obj):
    """
    function returns returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    :param obj: objected to be represented
    :return: JSON description of object
    """
    return obj.__dict__
