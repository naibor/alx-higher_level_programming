#!/usr/bin/python3
from sys import argv

if __name__ != "__main__":
    exit()

# number of arguments
number_of_args = len(argv)

count = 0
sum_of = 0
for arguments in argv:
    if count == 0:
        count = count + 1
    else:
        sum_of = sum_of + int(argv[count])
        count = count + 1
print("{}".format(sum_of))
