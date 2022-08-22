#!/usr/bin/env python3
import numpy as np
"""Write a class Neuron that defines a single
   neuron performing binary classification"""


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
