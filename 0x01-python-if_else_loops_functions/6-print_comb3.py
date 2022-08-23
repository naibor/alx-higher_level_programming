#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(num1 + 1, 10):
        if num1 == 8:
            print("{:d}{:d}".format(num1, num2))
            break
        print("{:d}{:d}".format(num1, num2), end=", ")
