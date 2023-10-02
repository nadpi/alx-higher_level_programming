#!/usr/bin/python3
""" A class """


class BaseGeometry:
    """ class BaseGeometry that has a public instance mtehod
    which raise an exception"""

    def area(self):
        raise Exception("area() is not implemented")
