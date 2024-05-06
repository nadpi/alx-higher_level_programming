#!/usr/bin/python3
'''Task 0'''


def read_file(filename=""):
    '''a function that reads a text file (UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="", file=sys.stdout)
    f.closed
