#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        i = ord(str[c])
        if i <= 123 and i >= 97:
            i = i - 32
            print("{}".format(chr(i)), end="")
        else:
            print("{}".format(chr(i)), end="")
