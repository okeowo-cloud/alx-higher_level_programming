#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary.get(key) is None:
        a_dictionary.setdefault(key, value)
    else:
        a_dictionary[key] = value
    return a_dictionary
