#!/usr/bin/python3
if __name__ != "__main__":
    exit()
from sys import argv
number_of_arguments = len(argv)
count = 0
if number_of_arguments == 1:
    print("{} arguments.".format(number_of_arguments - 1))
elif number_of_arguments > 1:
    print("{} arguments:".format(number_of_arguments - 1))
    for argument in argv:
        if count == 0:
            count = count + 1
        else:
            print("{}: {}".format(count, argv[count]))
            count = count + 1
