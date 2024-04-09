#!/usr/bin/python3
""" task 1"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """" returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calc area'''
        return self.__width * self.__height

    def perimeter(self):
        '''calc perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''print rect'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectstr = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectstr.append("#")
            if i < self.__height - 1:
                rectstr.append('\n')
        return ''.join(rectstr)
