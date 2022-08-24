#!/usr/bin/env python3
"""Neural Network"""
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork():
    "defines a neural network with one hidden layer"
    def __init__(self, nx, nodes):
        " Constructor method "
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=((1, nodes)))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """getter _W1"""
        return self.__W1

    @property
    def b1(self):
        """getter _b1"""
        return self.__b1

    @property
    def A1(self):
        """getter _A1"""
        return self.__A1

    @property
    def W2(self):
        """getter _W2"""
        return self.__W2

    @property
    def b2(self):
        """getter _b2"""
        return self.__b2

    @property
    def A2(self):
        """getter _A2"""
        return self.__A2

    def forward_prop(self, X):
        """Calculates the forward propagation of the neural network"""
        z1 = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = (1 / (1 + np.exp(-z1)))
        z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = (1 / (1 + np.exp(-z2)))
        return self.__A1, self.__A2

    def cost(self, Y, A):
        """cost function"""
        return ((-1/Y.shape[1]) * (np.sum(np.matmul(Y, np.log(A).transpose())
                + np.matmul((1-Y), np.log(1.0000001-A).transpose()))))

    def evaluate(self, X, Y):
        """Evaluates the neurons predictions"""
        self.forward_prop(X)
        evalu = np.where(self.__A2 >= 0.5, 1, 0)
        cost_y = self.cost(Y, self.__A2)
        return (evalu, cost_y)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """Calculates one pass of gradient descent on the neural network"""
        m = Y.shape[1]
        dz2 = A2 - Y
        dW2 = (1/m) * np.matmul(A1, dz2.T)
        db2 = (1/m) * np.sum(dz2, axis=1, keepdims=True)
        dz11 = np.matmul(self.__W2.T, dz2)
        dz12 = A1 * (1 - A1)
        dz1 = dz11 * dz12
        dw1 = (1/m) * np.matmul(dz1, X.T)
        db1 = (1/m) * np.sum(dz1, axis=1, keepdims=True)
        self.__W1 = self.__W1 - (alpha * dw1)
        self.__b1 = self.__b1 - (alpha * db1)
        self.__W2 = self.__W2 - (alpha * dW2).T
        self.__b2 = self.__b2 - (alpha * db2)

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """Trains the neural network"""
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose is True or graph is True:
            if type(step) is not int:
                raise TypeError("step must be an integer")
            if step < 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")
        aux = []
        for i in range(iterations + 1):
            self.__A1, self.__A2 = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)
            cost = self.cost(Y, self.__A2)
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
