#!/usr/bin/python3
def uppercase(_str):
    for a in _str:
        if 97 <= ord(a) <= 122:
            print("{}".format(chr(ord(a) - 32)), end="")
        else:
            print("{}".format(a), end="")
