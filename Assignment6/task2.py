import numpy as np
import matplotlib.pyplot as plt

# Data for Task 2
x = np.array([0, 2, 4, 6, 8])
y = np.array([1, 4, 16, 36, 64])

# Newton's Forward Difference Formula for Second Derivative
h = x[1] - x[0]
forward_diff_2 = (y[2] - 2 * y[1] + y[0]) / h**2

# Output the result
print("Task 2: Second Derivative at x=0 using Newton's Forward Difference Formula")
print("d²y/dx² =", forward_diff_2)

# Plotting
plt.plot(x, y, '-o', label='Data Points')
plt.axhline(forward_diff_2, color='g', linestyle='--', label='Second Derivative at x=0')
plt.title("Task 2: Second Derivative Using Forward Difference")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
