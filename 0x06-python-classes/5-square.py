#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ a class sqaure that has size
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ size: size

        size must be an integer,
        otherwise raise a TypeError except. with the msg size must be an int
        if size is less than 0,
        raise a ValueError exception with the message size must be >= 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #:
            if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
