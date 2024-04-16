#!/usr/bin/python3
''' 9. Full rectangle '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a class Rectangle that inherits from BaseGeometry '''
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' area method '''
        return self.__width * self.__height

    def __str__(self):
        ''' prints '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
