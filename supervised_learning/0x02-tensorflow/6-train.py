#!/usr/bin/env python3
"""6.Train"""
import tensorflow.compat.v1 as tf
calculate_accuracy = __import__('3-calculate_accuracy').calculate_accuracy
calculate_loss = __import__('4-calculate_loss').calculate_loss
create_placeholders = __import__('0-create_placeholders').create_placeholders
create_train_op = __import__('5-create_train_op').create_train_op
forward_prop = __import__('2-forward_prop').forward_prop


def train(X_train, Y_train, X_valid, Y_valid, layer_sizes, activations, alpha, iterations, save_path="/tmp/model.ckpt"):
    """builds, trains, and saves a neural network classifier"""
    for i in range(iterations):
        if i == 0 or i / 100 == 0:
            print(f"After {i} iterations:")
            cost = calculate_loss(Y_valid, Y_train)
            accuracy = calculate_accuracy(Y_valid, Y_train)
            print(f"\tTraining Cost: {cost}")
            print(f"\tTraining Accuracy: {accuracy}")
            print(f"\tValidation Cost: {cost}")
            print(f"\tValidation Accuracy: {accuracy}")