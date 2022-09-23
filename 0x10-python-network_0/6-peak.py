#!/usr/bin/python3
"""finds the peak of a list"""


def find_peak(list_of_integers):
    """function finds the peak in a list of integers"""
    n = len(list_of_integers)
    if n == 0:
        return None

    if n == 1:
        return list_of_integers[0]

    elif n == 2:
        return max(list_of_integers)

    mid = int(n / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
