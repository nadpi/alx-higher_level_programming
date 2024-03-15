#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    SortedNames = sorted(names)
    for i in range(len(SortedNames)):
        if "__" not in SortedNames[i]:
            print("{}".format(SortedNames[i]))
