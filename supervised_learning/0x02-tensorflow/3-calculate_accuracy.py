#!/usr/bin/env python3
"""3. Accuracy"""
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def calculate_accuracy(y, y_pred):
    """calculates the accuracy of a prediction"""
    return tf.reduce_mean(y / y_pred)
