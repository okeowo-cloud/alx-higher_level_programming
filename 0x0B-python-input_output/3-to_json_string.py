#!/usr/bin/python3
import json
"""3-to_json_string Module"""


def to_json_string(my_obj):
    """
    function returns JSON representation of an object (string)

    :param my_obj: String to serialize
    :return: Json representation

    """
    return (json.dumps(my_obj))
