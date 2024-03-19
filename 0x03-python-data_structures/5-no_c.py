#!/usr/bin/python3
def no_c(my_string):
    cp_string = ''
    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            cp_string += my_string[i]
    return cp_string
