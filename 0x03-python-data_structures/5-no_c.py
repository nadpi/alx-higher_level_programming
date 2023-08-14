#!/usr/bin/python3
def no_c(my_string):
    new_string = "".format()
    for c in range(len(my_string)):
        if my_string[c] == "c" or my_string[c] == "C":
            continue
        else:
            new_string += my_string[c]
    return new_string
