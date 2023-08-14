#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        newt = ((len(sentence), sentence[0]))
        return newt
    else:
        newt = ((len(sentence), None))
        return newt
