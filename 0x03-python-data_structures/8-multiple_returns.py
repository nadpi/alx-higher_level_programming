#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tup = (len(sentence), sentence[0])
        return tup
    else:
        tup = (len(sentence), None)
        return tup
