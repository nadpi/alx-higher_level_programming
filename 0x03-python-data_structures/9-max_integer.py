#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxNum = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > maxNum:
                maxNum = my_list[i]
        return maxNum
    else:
        return None
