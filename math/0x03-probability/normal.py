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
            for item in data:
                i += 1
                aux += item
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)