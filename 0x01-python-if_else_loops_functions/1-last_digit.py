#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((-number % 10) * -1)
# perform checks
if last_digit > 5:
    string = "and is greater than 5"
elif last_digit == 0:
    string = "and is 0"
elif last_digit < 6 and not 0:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, lastDigit), string)
