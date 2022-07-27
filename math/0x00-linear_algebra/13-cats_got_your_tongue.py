#!/usr/bin/env python3
import numpy as np
'''Write a function that concatenates two matrices along a specific axis:'''


def np_cat(mat1, mat2, axis=0):
    '''concatenates two matrices along a specific axis'''
    new = np.concatenate((mat1, mat2), axis=axis)
    return new
