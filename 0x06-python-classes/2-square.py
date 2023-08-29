#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ a class sqaure that has size
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
