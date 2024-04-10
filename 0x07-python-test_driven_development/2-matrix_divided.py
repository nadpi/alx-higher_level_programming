#!/usr/bin/python3
def matrix_divided(matrix, div):
    '''  a function that divides all elements of a matrix. '''
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        + "of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            + "of integers/floats")
    for j in matrix:
        for k in j:
            if not isinstance(k, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                + "of integers/floats")
    rowlen = len(matrix[0])
    for l in range(len(matrix)):
        if len(matrix[l]) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmatrix = []
    for n in range(len(matrix)):
        row = []
        for m in range(len(matrix[n])):
            row.append(round((matrix[n][m] / div), 2))
        newmatrix.append(row)
    return newmatrix
