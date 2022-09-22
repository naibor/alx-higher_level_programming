#!/usr/bin/python3
"""
Module matrix_divided
Divides a  matrix of numbers by a number
"""


def matrix_divided(matrix, div):
    """Matrix divided by a number
    Args:
        matrix(list): The matrix to divide
        div(int): What to divide by
    Exceptions:
        Raise TypeError if matrix is not a [[]] of type int or float
        Raise TypeError if row of matrix is not of same size
        Raise TypeError if div not int
        Raise ZeroDivisionError if div is 0
    Returns:
        Returns a new matrix
    """
    # handle exceptions
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for item in row:
            if type(item) != int:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    # check the argument div
    if type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # calculate division
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = round(item / div, 2)
            new_row.append(new_item)
        new_matrix.append(new_row)
    return new_matrix
