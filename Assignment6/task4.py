import numpy as np
import matplotlib.pyplot as plt

# Data for Task 4
x = np.array([1, 2, 4, 7])
y = np.array([3, 6, 12, 21])

# Target point
x_target = 3

# Lagrange's Interpolation Formula for Derivative
lagrange_diff = (
    ((x_target - x[1]) * (x_target - x[2])) / ((x[0] - x[1]) * (x[0] - x[2])) * y[0]
    + ((x_target - x[0]) * (x_target - x[2])) / ((x[1] - x[0]) * (x[1] - x[2])) * y[1]
    + ((x_target - x[0]) * (x_target - x[1])) / ((x[2] - x[0]) * (x[2] - x[1])) * y[2]
)

# Output the result
print("Task 4: Derivative at x=3 using Lagrange's Interpolation Formula")
print("dy/dx =", lagrange_diff)

# Plotting
plt.plot(x, y, '-o', label='Data Points')
plt.axhline(lagrange_diff, color='r', linestyle='--', label=f'Derivative at x={x_target}')
plt.title("Task 4: Derivative Using Lagrange's Formula")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
