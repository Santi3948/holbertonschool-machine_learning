#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

plt.yscale("log")

plt.axis([0, 28650, None, None])

plt.plot(x,y)

plt.title("Exponential Decay of C-14")

plt.ylabel('Fraction Remaining')

plt.xlabel('Time (years)')

plt.show()