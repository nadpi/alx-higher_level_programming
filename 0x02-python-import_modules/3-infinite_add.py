#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = 0
    if len(argv) == 1:
        print("0")
    elif len(argv) > 1:
        for i in range(1, len(argv)):
            res = res + int(argv[i])
        print("{}".format(res))
