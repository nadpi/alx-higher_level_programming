#!/usr/bin/python3
""" class my list that inherits from list """

class MyList(list):
    """ class my list """

    def print_sorted(self):
        a = []
        for i in range(len(self)):
            a.append(self[i])
        a.sort()
        print("[", end="")
        for i in range(len(self)):
            print(a[i], end="")
            if (i < len(self) - 1):
                print(", ", end="")
        print("]")
