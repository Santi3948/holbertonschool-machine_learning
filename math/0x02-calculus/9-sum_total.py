#!/usr/bin/env python3
'''Write a function def summation_i_squared(n):'''


def summation_i_squared(n):
    '''the function'''
    if (type(n) is not int) or (n is None):
        return None
    if n < 0 or n == 0:
        return None
    elif n == 1:
        return (n**2)
    else:
        return (summation_i_squared(n - 1) + (n**2))
