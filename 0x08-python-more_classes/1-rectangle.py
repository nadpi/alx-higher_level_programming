#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ class rect
    Attributes:
    width (int): width of rect
    height (int): heihgt of rect
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width: width
        must be int and >= 0 """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height: height
        height musr be int and >= 0"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
