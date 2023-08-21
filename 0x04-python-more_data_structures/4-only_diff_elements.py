#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1:
        if set_2:
            newset = set()
            for i in set_1:
                if i not in set_2:
                    newset.add(i)
            for i in set_2:
                if i not in set_1:
                    newset.add(i)
            return newset
        else:
            return set_1
    else:
        if set_2:
            return set_2
        else:
            return set_1
