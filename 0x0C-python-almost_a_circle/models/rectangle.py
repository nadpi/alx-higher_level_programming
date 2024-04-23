#!/usr/bin/python3
'''Task 3'''
from models.base import Base


class Rectangle(Base):
    '''class rect'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        '''set width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """" returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        '''set height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''returns x'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' set x'''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y'''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' area func'''
        return self.__height * self.__width

    def display(self):
        '''prints'''
        if self.__y:
            for k in range(self.__y):
                print()
        for i in range(self.__height):
            for l in range(self.__x):
                        print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''str'''
        strtoret = "[Rectangle] "+"("+str(self.id)+") "
        strtoret += str(self.__x)+"/"+str(self.__y)+" - "
        strtoret += str(self.__width)+"/"+str(self.__height)
        return strtoret
