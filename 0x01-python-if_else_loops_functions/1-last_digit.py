#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    newn = number * -1
else:
    newn = number

lastd = (newn % 10)

if lastd > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastd))
elif lastd < 6 and lastd != 0:
    print(f"Last digit of {number} is {lastd} and is less than 6 and not 0")
elif lastd == 0:
    print("Last digit of {} is {} and and is 0".format(number, lastd))
