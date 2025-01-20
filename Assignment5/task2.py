import numpy as np
import matplotlib.pyplot as plt

# Newton's Backward Interpolation
x = np.array([3, 4, 5, 6, 7])
y = np.array([2.2, 3.5, 5.1, 7.3, 10.0])

n = len(x)
difference_table = np.zeros((n, n))
difference_table[:, 0] = y

for j in range(1, n):
    for i in range(n - 1, j - 2, -1):
        difference_table[i][j] = difference_table[i][j - 1] - difference_table[i - 1][j - 1]

h = x[1] - x[0]
u = (5.5 - x[-1]) / h

# Calculating interpolated value
interpolated_value = difference_table[-1][0]
factorial = 1
u_term = 1

for i in range(1, n):
    u_term *= (u + (i - 1))
    factorial *= i
    interpolated_value += (u_term * difference_table[-1][i]) / factorial

# Print the result
print(f"Estimated value of f(5.5) using Newton's Backward Interpolation: {interpolated_value:.4f}")

# Plotting
plt.plot(x, y, 'o-', label="Given Data Points")
plt.axvline(5.5, color='red', linestyle='--', label="Interpolation Point")
plt.title("Newton's Backward Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
