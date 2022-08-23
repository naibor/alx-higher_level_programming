#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z')+1):
    if alphabets in [101, 113]:
        continue
    print("{:c}".format(alphabets), end="")
