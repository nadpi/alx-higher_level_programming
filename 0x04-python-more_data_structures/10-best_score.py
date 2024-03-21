#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxnum = 0
    whomaxnum = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > maxnum:
            maxnum = a_dictionary[i]
            whomaxnum = i
    return whomaxnum
