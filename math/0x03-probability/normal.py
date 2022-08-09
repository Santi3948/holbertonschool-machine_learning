#!/usr/bin/env python3
"""6. Initialize Normal"""


class Normal:
    """class Normal that represents a normal distribution"""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Class contructor"""
        if data or data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            i = 0
            aux = 0
            aux2 = 0
            for item in data:
                i += 1
                aux += item
            self.mean = float(aux/i)
            for item2 in data:
                aux2 += (item2 - self.mean) ** 2
            self.stddev = float(self.heron(aux2/i))
        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)

    def heron(self, n):
        """heron sequence"""
        prev = 0
        a = n / 2
        while True:
            a = (1/2) * (a + (n / a))
            if a == prev:
                break
            prev = a
        return float(a)

    def z_score(self, x):
        """Calculates the z-score of a given x-value"""
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """Calculates the x-value of a given z-score"""
        return ((self.stddev * z) + self.mean)
