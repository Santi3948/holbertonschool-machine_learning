#!/usr/bin/env python3
"""Write a class Neuron that defines a
   single neuron performing binary classification
"""
import numpy as np


class Neuron:
    """neuron performing binary classification"""
    def __init__(self, nx):
        """class constructor"""
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__b = 0
        self.__A = 0
        self.__W = np.random.randn(1, nx)

    @property
    def W(self):
        """getter _W"""
        return self.__W

    @property
    def A(self):
        """getter _A"""
        return self.__A

    @property
    def b(self):
        """getter _b"""
        return self.__b

    def forward_prop(self, X):
        """Calculates the forward propagation of the neuron"""
        z = np.matmul(self.__W, X) + self.__b
        self.__A = (1 / (1 + np.exp(-z)))
        return self.__A
