#!/usr/bin/python3
def weight_average(my_list=[]):
    elem_2_mul = [x * y for x, y in my_list]
    elem_2_div = [y for x, y in my_list]
    total, no_of_element = 0.0, 0.0
    for i in range(len(elem_2_div)):
        total += elem_2_mul[i]
        no_of_element += elem_2_div[i]
    return total / no_of_element
