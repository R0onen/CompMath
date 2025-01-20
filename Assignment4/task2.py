import numpy as np
import matplotlib.pyplot as plt

# Task 2: Polynomial Curve Fitting
x = np.array([0, 1, 2, 3, 4])
y = np.array([2, 3, 6, 11, 18])

# Compute coefficients a, b, c
coeff = np.polyfit(x, y, 2)
a, b, c = coeff
fit = a * x**2 + b * x + c

# Output results
print("Task 2: Polynomial Curve Fitting")
print(f"Coefficients:\n  a = {a:.2f}\n  b = {b:.2f}\n  c = {c:.2f}")
print("Fitted Curve: y =", a, "* x^2 +", b, "* x +", c)

# Plot Polynomial Fit
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='green', label='Data Points')
plt.plot(x, fit, label=f'Best Fit: y = {a:.2f}x² + {b:.2f}x + {c:.2f}', color='purple')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Curve Fitting')
plt.legend()
plt.grid()
plt.show()
