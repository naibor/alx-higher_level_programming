#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        ord_letter = ord(letter)
        if ord_letter in range(97, 123):
            ord_letter = ord_letter - 32
        print("{:c}".format(ord_letter), end="")
    print()
