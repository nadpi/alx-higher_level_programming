#!/usr/bin/python3
""" task 1"""


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        listy = self[:]
        listy.sort()
        print(listy)
