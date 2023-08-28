#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list:
        num = ""
        for i in range(x):
            try:
                num = num + str(my_list[i])
                print("{}".format(my_list[i]), end="")
            except IndexError:
                print("")
                return i
        print("")
        return i + 1
