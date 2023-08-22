#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sums = 0
        if roman_string[0] == "I":
            sums = -2
        for c in range(0, len(roman_string)):
            if roman_string[c] in roman:
                sums += roman[roman_string[c]]
        return sums
    else:
        return 0

