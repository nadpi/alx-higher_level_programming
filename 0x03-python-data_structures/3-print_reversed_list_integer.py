#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cnt = len(my_list) - 1
    for i in range(len(my_list)):
        print("{:d}".format(my_list[cnt]))
        cnt -= 1
