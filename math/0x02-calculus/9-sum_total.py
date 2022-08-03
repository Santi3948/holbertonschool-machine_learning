#!/usr/bin/env python3
'''Write a function def summation_i_squared(n):'''


def summation_i_squared(n):
    '''the function'''
    if (type(n) is not int):
        return None
    if n < 0 or n == 0:
        return None
    return int(((n * (n + 1) * (2*n + 1))/6))
