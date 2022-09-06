#!/usr/bin/env python3
"""1. Create Confusion"""
import numpy as np


def sensitivity(confusion):
    """ confusion is a confusion numpy.ndarray of shape (classes,
        classes) where row indices represent the correct labels and
        column indices represent the predicted labels
        classes is the number of classes
        Returns: a numpy.ndarray of shape (classes,) containing the
        sensitivity of each class
    """
    TP = np.diag(confusion)
    FP = confusion.sum(axis=0) - np.diag(confusion)
    FN = confusion.sum(axis=1) - np.diag(confusion)
    TN = confusion.sum() - (FP + FN + TP)

    P = TP + FN
    N = TN + FP

    sensitivity = TP / P

    return sensitivity
