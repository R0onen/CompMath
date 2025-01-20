import numpy as np
import matplotlib.pyplot as plt

# Central Difference Interpolation
x = np.array([10, 12, 14, 16, 18])
y = np.array([100, 144, 196, 256, 324])

n = len(x)
h = x[1] - x[0]
difference_table = np.zeros((n, n))
difference_table[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        difference_table[i][j] = difference_table[i + 1][j - 1] - difference_table[i][j - 1]

u = (13 - x[n // 2]) / h
interpolated_value = difference_table[n // 2][0]
u_term = 1
factorial = 1
k = n // 2

for i in range(1, n):
    if i % 2 == 0:
        k -= 1
    u_term *= (u + (-1)**i * (i // 2))
    factorial *= i
    interpolated_value += (u_term * difference_table[k][i]) / factorial

# Print the result
print(f"Estimated value of f(13) using Central Difference Interpolation: {interpolated_value:.4f}")

# Plotting
plt.plot(x, y, 'o-', label="Given Data Points")
plt.axvline(13, color='red', linestyle='--', label="Interpolation Point")
plt.title("Central Difference Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
