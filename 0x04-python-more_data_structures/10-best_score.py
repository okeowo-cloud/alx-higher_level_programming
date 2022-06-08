#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys) == 0:
        return None
    max_score = a_dictionary.get(list(a_dictionary.keys())[0])
    index = list(a_dictionary.keys())[0]
    for k in a_dictionary.keys():
        if a_dictionary.get(k) > max_score:
            max_score = a_dictionary.get(k)
            index = k
    return index
