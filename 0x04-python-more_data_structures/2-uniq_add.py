#!/usr/bin/python3
def uniq_add(my_list=[]):
    wasHere = []
    sumoflist = 0
    for i in range(len(my_list)):
        if my_list[i] not in wasHere:
            wasHere.append(my_list[i])
            sumoflist += my_list[i]
    return sumoflist
