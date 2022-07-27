#!/usr/bin/env python3
'''Write a function that calculates the shape of a matrix'''


def matrix_shape(matrix):
    '''this function calculates the matrix shape'''
    mat_shape = []
    while type(matrix) is list:
        mat_shape.append(len(matrix))
        matrix = matrix[0]
    return mat_shape
