#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1:
        if set_2:
            newset = set()
            flag = True
            for i in set_1:
                if i in set_2:
                    newset.add(i)
            return newset
        else:
            return set_1
    else:
        return set_1
