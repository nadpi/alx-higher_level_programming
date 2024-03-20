#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            if list(set_1)[i] == list(set_2)[j]:
                if list(set_2)[j] not in set_3:
                    set_3.add(list(set_2)[j])
    return set_3
