#!/usr/bin/python3
def safe_print_integer(value):
    try:
        try:
            print("{:d}".format(value))
        except ValueError:
            return False
        return True
    except TypeError:
        return False
