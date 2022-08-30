#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples

    Args:
        tuple_a: the first tuple
        tuple_b: the other one
    Returns:
        returns a tuple with 2 integers
        the first element is the sum first elements
        the second element is the sum of the second elements
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_tup = ()
    for i in range(2):
        if i >= len_a:
            a = 0
        else:
            a = tuple_a[i]
        if i >= len_b:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            new_tup = (a + b)
        else:
            new_tup = (new_tup, a + b)
    return (new_tup)
