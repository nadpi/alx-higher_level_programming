#!/usr/bin/python3
'''Class Square'''


class Square:
    ''' class square has
    Args:
        size(int): size
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        ''' return size '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        size must be an integer, otherwise raise a TypeError
        exception with the message size must be an integer
        if size is less than 0, raise a ValueError
        exception with the message size must be >= 0'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' returns the current square area'''
        return self.__size * self.__size

    def my_print(self):
        ''' prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()

