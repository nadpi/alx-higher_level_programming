#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict()
    for i in a_dictionary.keys():
        newdict.update({i: a_dictionary[i] * 2})
    return newdict
