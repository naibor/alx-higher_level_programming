#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ != "__main__":
    exit()

number_of_arguments = len(argv)
usage_error = "Usage: ./100-my_calculator.py <a> <operator> <b>"
operator_error = "Unknown operator. Available operators: +, -, * and /"

if number_of_arguments != 4:
    print("{}".format(usage_error))
    exit(1)
else:
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

if argv[2] == '+':
    answer = add(a, b)
elif argv[2] == '-':
    answer = sub(a, b)
elif argv[2] == '*':
    answer = mul(a, b)
elif argv[2] == '/':
    answer = div(a, b)
else:
    print("{}".format(operator_error))
    exit(1)
print("{} {} {} = {}".format(a, operator, b, answer))
