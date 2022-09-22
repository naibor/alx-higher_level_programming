#!/usr/bin/python3
"""
Module 100-matrix_mul
Multiplies two matrixes and get a new matrix
"""


def matrix_mul(m_a, m_b):
    """Multiply two  matrix
    Args:
        m_a: first matrix
        m_b: second matrix
    Raise:
        raise TypeError if m_a or m_b is not a list
        TypeError if m_a or m_b is not a list of lists
        ValueError if m_a or m_b is empty
        TypeError if values in m_a or m_b are not ints
        TypeError if length of list in m_a and m_b are not equal
        ValueError if m_a cant be multiplied with m_b
    """
    # handle exceptions
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_len = []
    for row in m_a:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_a must should be of the same size")
    row_len = []
    for row in m_b:
        row_len.append(len(row))
    if not all(elem == row_len[0] for elem in row_len):
        raise TypeError("each row of m_b must should be of the same size")

    a_row = 0
    for row in m_a[0]:
        a_row += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_row != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    # now multiply
    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
