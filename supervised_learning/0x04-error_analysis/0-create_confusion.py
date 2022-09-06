#!/usr/bin/env python3
"""0. Create Confusion"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """creates a confusion matrix"""
    m, classes = labels.shape
    mat_conf = np.zeros((classes, classes))
    labels = np.argmax(labels, axis=1)
    logits = np.argmax(logits, axis=1)
    for i in range(m):
        mat_conf[labels[i], logits[i]] += 1
    return mat_conf
