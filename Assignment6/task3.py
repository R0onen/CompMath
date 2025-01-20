import numpy as np
import matplotlib.pyplot as plt

# Data for Task 3
x = np.array([5, 6, 7, 8, 9])
y = np.array([10, 16, 26, 40, 58])

# Newton's Backward Difference Formula
h = x[1] - x[0]
backward_diff_1 = (y[-1] - y[-2]) / h

# Output the result
print("Task 3: First Derivative at x=9 using Newton's Backward Difference Formula")
print("dy/dx =", backward_diff_1)

# Plotting
plt.plot(x, y, '-o', label='Data Points')
plt.axhline(backward_diff_1, color='r', linestyle='--', label='First Derivative at x=9')
plt.title("Task 3: First Derivative Using Backward Difference")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
