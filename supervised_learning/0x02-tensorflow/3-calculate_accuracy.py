#!/usr/bin/env python3
"""3. Accuracy"""
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def calculate_accuracy(y, y_pred):
    """calculates the accuracy of a prediction"""
    equal = tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1))
    accuracy = tf.reduce_mean(tf.cast(equal, tf.float32))
    return accuracy
