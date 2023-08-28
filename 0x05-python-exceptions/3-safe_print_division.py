#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = 0
        try:
            res = a / b
        except ZeroDivisionError:
            res = None
        finally:
            print("inside result: {}".format(res))
        return res
    except TypeError:
        return None
