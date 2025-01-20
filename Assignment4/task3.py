import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Task 3: Exponential Curve Fitting
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.5, 4.7, 8.8, 16.2, 30.3])

# Define exponential function
def exp_func(x, a, b):
    return a * np.exp(b * x)

# Fit exponential model
params, _ = curve_fit(exp_func, x, y)
a, b = params

# Output results
print("Task 3: Exponential Curve Fitting")
print(f"Parameters:\n  a = {a:.2f}\n  b = {b:.2f}")
print("Fitted Model: y =", a, "* e^(", b, "* x )")

# Plot Exponential Fit
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='orange', label='Data Points')
plt.plot(x, exp_func(x, a, b), label=f'Best Fit: y = {a:.2f}e^({b:.2f}x)', color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Exponential Curve Fitting')
plt.legend()
plt.grid()
plt.show()
