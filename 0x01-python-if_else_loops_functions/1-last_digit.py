#!/usr/bin/python3
import random
numbers = random.randint(-10000, 10000)
if numbers > 0:
    if numbers % 10 > 5:
        print("Last digit of {a} is {b} and is greater than 5".format(a=numbers, b=numbers % 10))
    elif numbers % 10 == 0:
        print("Last digit of {a} is {b} and is 0".format(a=numbers, b=numbers % 10))
    else:
        print("Last digit of {a} is {b} and is less than 6 and not 0".format(a=numbers, b=numbers % 10))
else:
    if numbers % 10 == 0:
        print("Last digit of {a} is {b} and is 0".format(a=numbers, b=numbers % 10))
    else:
        print("Last digit of {a} is -{b} and is less than 6 and not 0".format(a=numbers, b=abs(numbers) % 10))

