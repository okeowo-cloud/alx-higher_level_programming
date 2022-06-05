#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    t_list = []
    for num in my_list:
        if num % 2 == 0:
            t_list.append(True)
        else:
            t_list.append(False)
    return t_list
