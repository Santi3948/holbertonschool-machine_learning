#!/usr/bin/env python3
'''Write a function that concatenates two matrices along a specific axis'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''concatenates two matrices along a specific axis'''
    if axis not in [0, 1]:
        return None
    aux = list(map(list, mat1))
    if axis == 0:
        if len(mat2[0]) != len(mat1[0]):
            return None
        for item in mat2:
            aux.append(item)
    elif axis == 1:
        if len(mat2) != len(mat1):
            return None
        i = 0
        for item in aux:
            item += mat2[i]
            i += 1
    return aux
