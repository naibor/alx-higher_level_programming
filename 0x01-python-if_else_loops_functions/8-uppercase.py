#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        ord_letter = ord(letter)
        if ord_letter in range(97, 123):
            ord_letter = ord_letter - 32
            letter = chr(ord_letter)
        else:
            letter
        print(letter, end="")
    print()
