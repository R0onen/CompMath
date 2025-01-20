import numpy as np
import matplotlib.pyplot as plt

# Data for Task 1
x = np.array([0, 2, 4, 6, 8])
y = np.array([1, 4, 16, 36, 64])

# Newton's Forward Difference Formula
h = x[1] - x[0]
forward_diff_1 = (y[1] - y[0]) / h

# Output the result
print("Task 1: First Derivative at x=0 using Newton's Forward Difference Formula")
print("dy/dx =", forward_diff_1)

# Plotting
plt.plot(x, y, '-o', label='Data Points')
plt.axhline(forward_diff_1, color='r', linestyle='--', label='First Derivative at x=0')
plt.title("Task 1: First Derivative Using Forward Difference")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
