#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1:
        if set_2:
            newset = set()
            for i in set_1:
                if i in set_2:
                    newset.add(i)
            return newset
        else:
            return set_2
    else:
        return set_1
