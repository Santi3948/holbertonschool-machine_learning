#!/usr/bin/env python3
"""1. Layers"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """returns two placeholders, x and y, for the neural network:"""
    linear_model = tf.layers.Dense(name="layer", units=n,
                                   activation=activation)
    y = linear_model(prev)
    init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    return y
