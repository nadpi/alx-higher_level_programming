#!/usr/bin/python3
''' 7. Integer validator '''


class BaseGeometry:
    '''class BaseGeometry'''
    def area(self):
        '''raises an Exception with the message area() is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
