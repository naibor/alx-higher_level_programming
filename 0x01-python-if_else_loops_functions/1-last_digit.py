#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# get string representation
number_str = repr(number)
# get last digit
last_digit = int(number_str[-1])
# check if number is negative
if number < 0:
    last_digit = last_digit * -1
# perform checks
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif last_digit < 6 and not 0:
    print("Last digit of", number, "is", last_digit,
          "and is less than 6 and not 0")
