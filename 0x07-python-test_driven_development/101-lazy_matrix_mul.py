#!/usr/bin/python3
""" 
Module lazy_matrix_mul
It multiplies two matrixes using numpy
"""


import numpy
def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using
    Args:
        m_a: first matrix
        m_b: second matrix
    """
    return numpy.matmul(m_a, m_b)
