import numpy as np
import matplotlib.pyplot as plt

# Newton's Divided Difference
x = np.array([0, 2, 5, 8])
y = np.array([4, 8, 14, 25])

n = len(x)
divided_diff = np.zeros((n, n))
divided_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        divided_diff[i][j] = (divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]) / (x[i + j] - x[i])

target = 3
interpolated_value = divided_diff[0, 0]
for i in range(1, n):
    term = divided_diff[0, i]
    for j in range(i):
        term *= (target - x[j])
    interpolated_value += term

# Print the result
print(f"Estimated value of f(3) using Newton's Divided Difference: {interpolated_value:.4f}")

# Plotting
plt.plot(x, y, 'o-', label="Given Data Points")
plt.axvline(3, color='red', linestyle='--', label="Interpolation Point")
plt.title("Newton's Divided Difference")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
