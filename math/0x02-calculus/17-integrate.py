#!/usr/bin/env python3
'''Write a function that calculates the integral of a polynomial:'''


def poly_integral(poly, C=0):
    '''the function'''
    aux = []
    if (not all(isinstance(n, int) or isinstance(n, float) for n in poly)) \
            or (type(C) is not int):
        return None
    aux.append(C)
    for i in range(1, len(poly)):
        trunc = float(poly[i]) / float(i + 1)
        if trunc == int(trunc):
            aux.append(int(trunc))
        else:
            aux.append(float(poly[i]) / float(i + 1))
    return aux
