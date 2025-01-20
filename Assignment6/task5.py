import numpy as np
import matplotlib.pyplot as plt

# Data for Task 5
x = np.array([2, 4, 6, 8, 10])
y = np.array([5, 7, 8, 6, 3])

# Find maxima or minima
maxima_minima_x = x[np.argmax(y)]

# Output the result
print("Task 5: Maxima or Minima of the Tabulated Function")
print("x where y has maximum =", maxima_minima_x)

# Plotting
plt.plot(x, y, '-o', label='Data Points')
plt.axvline(maxima_minima_x, color='r', linestyle='--', label='Maxima/Minima')
plt.title("Task 5: Maxima or Minima of Tabulated Function")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
