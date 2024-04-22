#!/usr/bin/python3
'''Task 3'''
from models.base import Base


class Rectangle(Base):
    '''class rect'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
