#!/usr/bin/env python3
'''Write a function that adds two matrices element-wise:'''


def add_matrices2D(mat1, mat2):
    '''add matrices'''
    if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
        return None
    new_list = []
    for block1, block2 in zip(mat1, mat2):
        aux = []
        for item1, item2 in zip(block1, block2):
            aux.append(item1 + item2)
        new_list.append(aux)
    return new_list
