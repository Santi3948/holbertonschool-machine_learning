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

    def cost(self, Y, A):
        """Calculates the cost of the model using logistic regression"""
        return ((-1/Y.shape[1]) * (np.sum(np.matmul(Y, np.log(A).transpose())
                + np.matmul((1-Y), np.log(1.0000001-A).transpose()))))

    def evaluate(self, X, Y):
        """Evaluates the neuron’s predictions"""
        self.__A = self.forward_prop(X)
        eval = np.where(self.__A >= 0.5, 1, 0)
        return eval, self.cost(Y, self.__A)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculates one pass of gradient descent on the neuron"""
        a = A - Y
        m = 1 / Y.shape[1]
        self.__W = self.__W - (m) * alpha * np.matmul(X, a.transpose())
        self.__b = self.__b - (m) * alpha * np.sum(a)
