#!/usr/bin/env python3
'''Write a function that concatenates two matrices along a specific axis'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''concatenates two matrices along a specific axis'''
    if axis not in [0, 1]:
        return None
    aux = list(map(list, mat1))
    if axis not in [0, 1]:
        return None
    if axis == 0:
        for item in mat2:
            aux.append(item)
    elif axis == 1:
        i = 0
        for item in aux:
            item += mat2[i]
            i += 1
    return aux
