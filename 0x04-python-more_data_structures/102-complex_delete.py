#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = []
    for i in a_dictionary.keys():
        if a_dictionary.get(i) == value:
            tmp.append(i)
    for item in tmp:
        del a_dictionary[item]
    return a_dictionary
