#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cnt = len(my_list)
    for i in range(len(my_list)):
        cnt -= 1
        print("{:d}".format(my_list[cnt]))
