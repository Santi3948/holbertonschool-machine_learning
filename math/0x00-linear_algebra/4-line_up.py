#!/usr/bin/env python3
'''Write a function that adds two arrays element-wise'''


def add_arrays(arr1, arr2):
    '''add arrays'''
    if len(arr1) != len(arr2):
        return None
    new_list = []
    for item1, item2 in zip(arr1, arr2):
        new_list.append(item1 + item2)
    return new_list
