#!/usr/bin/env python3
'''Write a function def summation_i_squared(n):'''


def summation_i_squared(n):
    '''the function'''
    try:
        val = int(n)
    except ValueError:
        return None
    if n < 0 or n == 0:
        return 0
    else:
        return (summation_i_squared(n - 1) + (n**2))
