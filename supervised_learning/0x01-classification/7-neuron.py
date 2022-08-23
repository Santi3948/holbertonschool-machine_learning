#!/usr/bin/env python3
"""Write a class Neuron that defines a
   single neuron performing binary classification
"""
import numpy as np
import matplotlib.pyplot as plt


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
        m = Y.shape[1]
        dz = A - Y
        dw = (1/m) * np.matmul(X, dz.T)
        db = (1/m) * np.sum(dz)
        self.__W = self.__W - (alpha * dw).T
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        " Training the neuron with graph"
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations < 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha < 0:
            raise ValueError("alpha must be positive")
        if verbose is True or graph is True:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        aux = []
        for i in range(iterations + 1):
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            cost = self.cost(Y, self.__A)
            if verbose is True:
                if (i % step == 0 or step == iterations):
                    print("Cost after {} iterations: {}".format(i, cost))
                    if i < iterations:
                        aux.append(cost)
        if graph is True:
            x_list = np.arange(0, iterations, step)
            y_list = aux
            plt.plot(x_list, y_list)
            plt.title('Training Cost')
            plt.xlabel('iterations')
            plt.ylabel('cost')
            plt.show()
        return self.evaluate(X, Y)
