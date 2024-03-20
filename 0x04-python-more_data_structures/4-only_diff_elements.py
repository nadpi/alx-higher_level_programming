#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for i in range(len(set_1)):
        if list(set_1)[i] not in set_2:
            set_3.add(list(set_1)[i])
    for i in range(len(set_2)):
        if list(set_2)[i] not in set_1:
            set_3.add(list(set_2)[i])
    return set_3
