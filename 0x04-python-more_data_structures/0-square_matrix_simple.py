#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        newmatrix = []
        for j in range(len(matrix)):
            newmatrixrow = list(map((lambda x: x ** 2), matrix[j]))
            newmatrix.append(newmatrixrow)
        return newmatrix
    else:
        return matrix
