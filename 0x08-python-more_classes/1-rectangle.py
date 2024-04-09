#!/usr/bin/python3
''' Class Rectangle '''


class Rectangle:
    ''' MyClass rectangle
    Args:
        width (int): width
        height(int): height
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' retrieve width'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' check width for setting'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        ''' retrieve height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' check height for setting'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be an integer")
        self.__height = value
