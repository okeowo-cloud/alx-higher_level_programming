#!/usr/bin/python3
"""9-student Module"""


class Student:
    """Represent a Student object"""
    def __init__(self, first_name, last_name, age):
        """
        initialize a Student
        :param first_name: first name of student
        :param last_name: last name of student
        :param age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """
            defines the dictionary description of an instantiated student
            :return: dict description of student
            """
            return self.__dict__
