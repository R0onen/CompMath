import numpy as np
import matplotlib.pyplot as plt

# Lagrange's Interpolation
x = np.array([2, 5, 8, 10])
y = np.array([1.4, 2.3, 3.8, 4.6])

target = 6
n = len(x)
interpolated_value = 0

for i in range(n):
    term = y[i]
    for j in range(n):
        if i != j:
            term *= (target - x[j]) / (x[i] - x[j])
    interpolated_value += term

# Print the result
print(f"Estimated value of f(6) using Lagrange's Interpolation: {interpolated_value:.4f}")

# Plotting
plt.plot(x, y, 'o-', label="Given Data Points")
plt.axvline(6, color='red', linestyle='--', label="Interpolation Point")
plt.title("Lagrange's Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
