#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    newlist = [] * list_length
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            newlist.append(res)
        except ZeroDivisionError:
            res = 0
            newlist.append(res)
            print("division by 0")
        except TypeError:
            print("wrong type")
            res = 0
            newlist.append(res)
        except IndexError:
            res = 0
            newlist.append(res)
            print("out of range")
    return newlist
