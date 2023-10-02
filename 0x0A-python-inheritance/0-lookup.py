#!/usr/bin/python3
""" a function that returns the list of
available attributes and methods of an object """


def lookup(obj):
    """ Prototype: def lookup(obj):
    Returns a list object """
    return list(dir(obj))
