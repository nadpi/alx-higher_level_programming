#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ a class sqaure that has size
    Attributes:
        size (int): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ position: position
        position must be a tuple of 2 positive integers,
        otherwise raise a TypeError  with a specific msg"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ prints in stdout the square with the character #:
            if size is equal to 0, print an empty line"""
        if self.__size == 0:
            print("")
        else:
            for o in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
