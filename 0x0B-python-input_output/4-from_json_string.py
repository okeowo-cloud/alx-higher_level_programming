#!/usr/bin/python3
"""4-from_json_string Module"""
import json


def from_json_string(my_str):
    """
    function deserialize an object to Python data structure represented
    as JSON

    :param my_str: object to deserialize
    :return: the deserialized object

    """
    return json.loads(my_str)
