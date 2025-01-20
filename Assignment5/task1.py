import numpy as np
import matplotlib.pyplot as plt

# Newton's Forward Interpolation
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2.7, 5.8, 10.4, 16.5])

# Calculating forward differences
n = len(x)
difference_table = np.zeros((n, n))
difference_table[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        difference_table[i][j] = difference_table[i + 1][j - 1] - difference_table[i][j - 1]

h = x[1] - x[0]
u = (2.5 - x[0]) / h

# Calculating interpolated value
interpolated_value = difference_table[0][0]
factorial = 1
u_term = 1

for i in range(1, n):
    u_term *= (u - (i - 1))
    factorial *= i
    interpolated_value += (u_term * difference_table[0][i]) / factorial

# Print the result
print(f"Estimated value of f(2.5) using Newton's Forward Interpolation: {interpolated_value:.4f}")

# Plotting
plt.plot(x, y, 'o-', label="Given Data Points")
plt.axvline(2.5, color='red', linestyle='--', label="Interpolation Point")
plt.title("Newton's Forward Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
