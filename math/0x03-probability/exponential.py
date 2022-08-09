#!/usr/bin/env python3
"""3. Initialize Exponential"""


class Exponential:
    """Exponential that represents an exponential distribution"""
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
            self.lambtha = float(1/(aux/i))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
