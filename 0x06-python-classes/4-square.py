#!/usr/bin/python3
'''Class Square'''


class Square:
    ''' class square has
    Args:
        size(int): size
    '''
    def __init__(self, size=0):
        self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def size(self):
        return self.__size

    def area(self):
        ''' returns the current square area'''
        return self.__size * self.__size
