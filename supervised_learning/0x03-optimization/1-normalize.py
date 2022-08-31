#!/usr/bin/env python3
"""1. Normalize"""
import numpy as np


def normalize(X, m, s):
    """normalizes (standardizes) a matrix"""
    X = (X - m) / s
    return X
