#!/usr/bin/python3
""" task 6"""


class BaseGeometry:
    """ class basegemoetry"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
