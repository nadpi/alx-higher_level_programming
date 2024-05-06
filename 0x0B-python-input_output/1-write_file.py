#!/usr/bin/python3
'''Task 1'''


def write_file(filename="", text=""):
    '''a function that writes a string to a text file (UTF8)
    and returns the number of characters written'''
    with open(filename, 'w', encoding="utf-8") as f:
        words = f.write(text)
    f.closed
    return words
