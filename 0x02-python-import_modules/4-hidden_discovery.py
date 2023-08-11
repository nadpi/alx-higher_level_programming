#!/usr/bin/python3
if __name__ == "__main__":
    from os import path
    from sys import argv
    import hidden_4
    words = dir(hidden_4)
    for word in words:
        if word[0] != "_":
            print("{}".format(word))
