#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    for i in range(2):
        if i < len(tuple_a):
            if i < len(tuple_b):
                tuple_c = tuple_c+((tuple_a[i]+tuple_b[i]), )
            else:
                tuple_c = tuple_c + ((tuple_a[i]), )
        else:
            if i < len(tuple_b):
                tuple_c = tuple_c + ((tuple_b[i]), )
            else:
                tuple_c = tuple_c + ((0), )
    return tuple_c

