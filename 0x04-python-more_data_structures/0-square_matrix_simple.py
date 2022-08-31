#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Square values of matrix
    Args:
        matrix: the matrix to work on
    Returns:
        a new matrix
    """

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = item ** 2
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
