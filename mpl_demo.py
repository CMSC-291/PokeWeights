import csv
import matplotlib.pyplot as plt
import numpy as np

# Plotting x^2 the pure Python way
x = [2, 4, 6, 8, 10]
y = []

for num in x:
    y.append(num ** 2)

# Using numpy, this is WAY BETTER
x = np.linspace(0, 10, num=20)  # generates a list of 20 numbers from 0 to 10
y = x ** 2  # this actually squares every number in X!

plt.plot(x, y)
plt.show()

