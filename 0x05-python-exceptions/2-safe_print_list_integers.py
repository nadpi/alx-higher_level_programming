#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                print("")
                return i
            except IndexError:
                raise
        print("")
        return x
    except TypeError:
        return 0
