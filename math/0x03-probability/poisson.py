#!/usr/bin/env python3
"""0. Initialize Poisson"""


class Poisson:
    """class Poisson that represents a poisson distribution"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Class contructor"""
        if data or data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            i = 0
            aux = 0
            for item in data:
                i += 1
                aux += item
            if float(aux/i) <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(aux/i)
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def factorial(self, x):
        """factorial function"""
        if x == 0:
            return 1
        return (self.factorial(x - 1) * x)

    def pmf(self, k):
        """Calculates the value of the PMF for a given number of “successes”"""
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        return ((self.e ** (-self.lambtha)) * ((self.lambtha) ** k)
                / self.factorial(k))

    def cdf(self, k):
        """Calculates the value of the CDF for a given number of “successes”"""
        aux = 0
        for i in range(k+1):
            aux += self.pmf(i)
        return aux
