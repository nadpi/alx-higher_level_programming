#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        newm = matrix[:]
        for i in range(len(matrix)):
            newm.append('[')
            for j in range(len(matrix[i])):
                newm.append(matrix[i][j]**2)
                if j < len(matrix[i]):
                    newm.append[","]
                    newm.append[" "]
            if i < len(matrix):
                newm.append(']')
        return newm
    else:
        return matrix
