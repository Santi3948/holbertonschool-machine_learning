#!/usr/bin/env python3
"""5. Create Train"""
import tensorflow.compat.v1 as tf


def create_train_op(loss, alpha):
    """creates the training operation for the network"""
    optimizer = tf.train.GradientDescentOptimizer(alpha)
    train = optimizer.minimize(loss)
    return train
