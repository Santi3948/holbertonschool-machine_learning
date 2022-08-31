#!/usr/bin/env python3
"""0. Normalization Constants"""
import numpy as np
import tensorflow.compat.v1 as tf


def normalization_constants(X):
    """ calculates the normalization (standardization) constants of a matrix"""
    mean = sum(X) / np.shape(X)[0]
    standard_deviation = np.sqrt(sum((X - mean) ** 2) / np.shape(X)[0])
    return mean, standard_deviation
