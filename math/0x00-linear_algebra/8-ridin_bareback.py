#!/usr/bin/env python3
'''Write a function that performs matrix multiplication'''


def mat_mul(mat1, mat2):
    '''matrix multiplication'''
    if len(mat1[0]) != len(mat2):
        return None
    width = len(mat2[0])
    height = len(mat2)
    new_mat = []
    for i in range(width):
        new_mat2 = []
        for block in mat2:
            new_mat2.append(block[i])
        new_mat.append(new_mat2)
    mul = []
    for item1 in mat1:
        aux = []
        for item2 in new_mat:
            x = 0
            for i in range(len(mat1[0])):
                x += item1[i] * item2[i]
            aux.append(x)
        mul.append(aux)
    return mul
