#!/usr/bin/python3.8
import hidden_4
if __name__ != "__main__":
    exit()
defined_names = dir(hidden_4)

for name in defined_names:
    if name.startswith('__'):
        continue
    else:
        print("{}".format(name))
