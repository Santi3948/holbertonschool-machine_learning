#!/usr/bin/env python3
"""2. Shuffle Data"""
import numpy as np


def shuffle_data(X, Y):
    """shuffles the data points in two matrices the same way"""
    shuffler = np.random.permutation(len(X))
    x_shuffled = X[shuffler]
    y_shuffled = Y[shuffler]
    return x_shuffled, y_shuffled
