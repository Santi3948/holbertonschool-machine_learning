#!/usr/bin/env python3
"""10. Initialize Binomial"""


class Binomial:
    """class Binomial that represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """Class contructor"""
        if data or data is not None:
            aux = 0
            i = 0
            aux2 = 0
            for item in data:
                aux += item
                i += 1
            m = aux / i
            for item2 in data:
                aux2 += (item2 - m) ** 2
            x = aux2 / i
            self.p = float(1 - (x / m))
            self.n = round(m / self.p)
            self.p = float(m / self.n)
        else:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p < 0 or p > 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = p

    def factorial(self, x):
        """factorial function"""
        if x == 0:
            return 1
        return (self.factorial(x - 1) * x)