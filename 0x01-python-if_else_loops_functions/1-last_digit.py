#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

temp = number
# check if number is negative
if number < 0:
    number = -(number)

last_digit = number % 10
if temp < 0:
    number = temp
    last_digit = -(last_digit)

# perform checks
if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
elif last_digit < 6 and not 0:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastDigit), string)
