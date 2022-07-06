#!/usr/bin/python3
"""1-my_list Module"""


class MyList(list):
    """
    Representation of an arbitrary list which inherit from
    python list
    """

    def print_sorted(self):
        """
        print instances of myList in ascending order
        :return: void
        """
        tmp = self.copy()
        tmp.sort()
        print(tmp)
