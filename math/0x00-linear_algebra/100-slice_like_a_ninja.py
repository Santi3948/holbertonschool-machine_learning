#!/usr/bin/env python3
'''Write a function that slices a matrix along specific axes:'''

def np_slice(matrix, axes={}):
    dim = matrix.ndim
    print(f'{dim} dimension')
    new = matrix.copy()
    '''slice the matrix'''
    for item in sorted(axes):
        print(f'{item} axes')
        aux = matrix.copy()
        for item2 in range(0, sorted(axes)[len(sorted(axes)) - 1] + 1):
            print(f'{item2} order axes')
            if item2 == item:
                if item2 == (dim - 1):
                    print(f'aaaaaa {aux} que lokkkeee')
                else:
                    print("no soy dimension")
            aux = aux[0]
    return new