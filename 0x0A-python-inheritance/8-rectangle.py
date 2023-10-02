#!/usr/bin/python3
""" A class """


class BaseGeometry:
    """ class BaseGeometry that has a public instance mtehod
    which raise an exception"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry 
    Attributes:
    width (int): width
    hieght(int): height
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
