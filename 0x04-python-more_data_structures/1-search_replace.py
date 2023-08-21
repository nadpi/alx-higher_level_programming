#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        newlist = my_list[:]
        for i in range(len(newlist)):
            if newlist[i] == search:
                newlist[i] = replace
            else:
                continue
        return newlist
    else:
        return my_list
