#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxi = 0
        key = 0
        for k, v in a_dictionary.items():
            if v > maxi:
                maxi = v
                key = k
        return key
    else:
        return None
