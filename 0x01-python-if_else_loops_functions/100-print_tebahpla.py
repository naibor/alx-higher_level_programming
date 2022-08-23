#!/usr/bin/python3

for alphabet in reversed(range(97, 123)):
    if alphabet % 2:
        letter = alphabet - 32
        print("{:c}".format(letter), end="")
    else:
        print("{:c}".format(alphabet), end="")
