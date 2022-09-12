#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safe print a list
    Args:
        my_list: the list to print
        x: number of elements to print
    Returns:
        Returns the real number of elements printed
    """
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except:
            continue
    print()
    return count
