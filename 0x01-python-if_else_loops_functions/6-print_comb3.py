#!/usr/bin/python3
for i in range(1, 100, 11):
    for k in range(i, ((i // 10) * 10) + 10):
        if i < 89:
            print("{:02d}, ".format(k), end="")
        else:
            print("{}".format(89))

