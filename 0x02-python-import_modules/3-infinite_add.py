#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sums = 0
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print("{}".format(argv[1]))
    else:
        for i in range(1, len(argv)):
            sums += int(argv[i])
        print("{}".format(sums))
