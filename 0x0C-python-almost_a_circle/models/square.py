#!/usr/bin/python3
''' Task 10'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''prints'''
        strtoret = "[Square]"+" ("+str(self.id)+") "
        strtoret += str(self.x)+"/"+str(self.y)+" - "
        strtoret += str(self.width)
        return strtoret

    @property
    def size(self):
        '''ret size'''
        return self.width

    @size.setter
    def size(self, value):
        '''set size'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
