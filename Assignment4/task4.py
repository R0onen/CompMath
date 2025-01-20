import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Task 4: Logarithmic and Quadratic Model
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.6, 6.3, 11.5, 18.9])

# Define the model
def log_quad_func(x, a, b, c):
    return a + b * np.log(x) + c * x**2

# Fit model
params, _ = curve_fit(log_quad_func, x, y)
a, b, c = params

# Output results
print("Task 4: Logarithmic and Quadratic Model")
print(f"Parameters:\n  a = {a:.2f}\n  b = {b:.2f}\n  c = {c:.2f}")
print("Fitted Model: y =", a, "+", b, "* ln(x) +", c, "* x^2")

# Plot Logarithmic + Quadratic Fit
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, log_quad_func(x, a, b, c), label=f'Fit: y = {a:.2f} + {b:.2f}ln(x) + {c:.2f}x²', color='brown')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Logarithmic and Quadratic Model')
plt.legend()
plt.grid()
plt.show()
