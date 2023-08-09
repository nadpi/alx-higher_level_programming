#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        newn = number * -1
        lastd = (newn % 10)
    else:
        newn = number
        lastd = (newn % 10)

    print("{}".format(lastd), end="")
    return lastd
