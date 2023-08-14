#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newt = ()
    for i in range(2):
        if i < len(tuple_a):
            if i < len(tuple_b):
                newt = newt+((tuple_a[i]+tuple_b[i]), )
            else:
                newt = newt + ((tuple_a[i]), )
        else:
            if i < len(tuple_b):
                newt = newt + ((tuple_b[i]), )
            else:
                newt = newt + ((0), )
    return newt
