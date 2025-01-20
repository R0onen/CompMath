import numpy as np
import matplotlib.pyplot as plt

# Task 1: Linear Curve Fitting
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 8, 11, 15])

# Compute slope (m) and intercept (c)
coeff = np.polyfit(x, y, 1)
m, c = coeff
fit = m * x + c

# Output results
print("Task 1: Linear Curve Fitting")
print(f"Slope (m): {m:.2f}")
print(f"Intercept (c): {c:.2f}")
print("Fitted Line: y =", m, "* x +", c)

# Plot Linear Fit
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, fit, label=f'Best Fit: y = {m:.2f}x + {c:.2f}', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Curve Fitting')
plt.legend()
plt.grid()
plt.show()
