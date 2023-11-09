#!/usr/bin/python3
""" task 6"""


class BaseGeometry:
    """ class basegemoetry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value


class Rectangle(BaseGeometry):
    """ inherits from basegeom"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", width)
