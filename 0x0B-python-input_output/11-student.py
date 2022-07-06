#!/usr/bin/python3
"""10-student Module"""


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

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        :return: dict description of student
        """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        :param json: dictionary representation of student instance
        :return: void
        """
        for k, v in json.items():
            setattr(self, k, v)
