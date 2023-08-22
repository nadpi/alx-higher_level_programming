#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == False:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sums = 0
    for c in range(len(roman_string)):
        if roman_string[c] in roman:
            sums += roman[roman_string[c]]
        else:
            continue
    if roman_string[0] == "I":
        sums = sums - 2
    return sums

