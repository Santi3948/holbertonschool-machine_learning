#!/usr/bin/env python3
'''Write a function that calculates the derivative of a polynomial:'''


def poly_derivative(poly):
    '''the function'''
    aux = []
    if (type(poly) is not list) or (not all(isinstance(n, int) or isinstance(n, float) for n in poly)) or (len(poly) == 0):
        return None
    for i in range(1, len(poly)):
        aux.append(i * poly[i])
    if all(a == 0 for a in aux):
        return [0]
    return aux
