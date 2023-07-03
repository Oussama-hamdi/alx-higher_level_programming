#!/usr/bin/python3
"""A matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list
        div (int or float): Divisor

    Returns:
        list: A new matrix with all elements divided

    Raises:
        TypeError: If the matrix is not a list of lists of ints and floats.
        TypeError: If the divisor not a number.
        ZeroDivisionError: If the divisor == 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(ele / div, 2) for ele in row]
        new_matrix.append(new_row)

    return new_matrix
