#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_a = []
    for num in my_list:
        if num == search:
            num = replace
        list_a.append(num)
    return list_a
