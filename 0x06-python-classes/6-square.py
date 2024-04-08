#!/usr/bin/python3
'''Class Square'''


class Square:
    ''' class square has
    Args:
        size(int): size
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''return position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''position must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception
        with the message position must be a tuple of 2 positive integers'''
        if type(value) is not tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            for i in range(len(value)):
                if value[i] < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' returns the current square area'''
        return self.__size * self.__size

    def my_print(self):
        ''' prints in stdout the square with the character #'''
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                if self.__position:
                    for l in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
