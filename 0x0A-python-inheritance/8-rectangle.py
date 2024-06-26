#!/usr/bin/python3
''' 8. Rectangle '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a class Rectangle that inherits from BaseGeometry '''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
