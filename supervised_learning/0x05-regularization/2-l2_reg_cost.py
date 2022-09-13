#!/usr/bin/env python3
"""regularization of a model"""
import tensorflow.compat.v1 as tf


def l2_reg_cost(cost):
    """calculates the cost of a neural network L2
    """
    return cost + tf.compat.v1.losses.get_regularization_loss()
