#!/usr/bin/python3

def print_last_digit(number):
    str_num = repr(number)
    last_digit = str_num[-1]
    print("{}".format(int(last_digit)), end="")
    return int(last_digit)
