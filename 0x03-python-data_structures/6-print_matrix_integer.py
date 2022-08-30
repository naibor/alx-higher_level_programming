#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix[[]]: the matrix to print
    """
    for item in matrix:
        for num in item:
            print("{:d}".format(num), end=" ")
        print()
