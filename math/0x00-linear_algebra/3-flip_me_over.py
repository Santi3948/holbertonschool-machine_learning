#!/usr/bin/env python3
'''Write a function that returns the transpose of a 2D matrix, matrix'''


def matrix_transpose(matrix):
    '''this function transpose a matrix'''
    width = len(matrix[0])
    height = len(matrix)
    new_mat = []
    for i in range(width):
        new_mat2 = []
        for block in matrix:
            new_mat2.append(block[i])
        new_mat.append(new_mat2)
    return new_mat
