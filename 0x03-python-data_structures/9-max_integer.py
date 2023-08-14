#!/usr/bin/python3
def max_integer(my_list=[]):
    maxnum = my_list[0]
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] > maxnum:
                maxnum = my_list[i]
            else:
                continue
        return maxnum
    else:
        return None
