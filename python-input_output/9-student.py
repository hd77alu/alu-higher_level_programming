#!/usr/bin/python3
""" class Student + json"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize class

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function to get a dictionary representation of the Student."""
        return self.__dict__
