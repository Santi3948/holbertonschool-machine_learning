#!/usr/bin/env python3
'''Write a function that calculates the integral of a polynomial:'''


def poly_integral(poly, C=0):
    '''the function'''
    aux = []
    if (type(C) is not int) or (type(poly) is not list) or (len(poly) == 0):
        return None
    if not all(isinstance(n, int) or isinstance(n, float) for n in poly):
        return None
    aux.append(C)
    for i in range(0, len(poly)):
        if i == 0 and poly[i] == 0:
            continue
        trunc = float(poly[i] / (i + 1))
        if trunc == int(trunc):
            aux.append(int(trunc))
        else:
            aux.append(trunc)
    for j in range(len(aux) - 1, 0, -1):
        if aux[j] != 0:
            break
        aux.pop(j)
    return aux
