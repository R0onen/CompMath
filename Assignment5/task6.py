import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import CubicSpline

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.3, 3.1, 4.9, 6.5, 8.1])

cs = CubicSpline(x, y)
points = [2.5, 4.3]

for point in points:
    print(f"Estimated value of f({point}) using Cubic Spline Interpolation: {cs(point):.4f}")

# Plotting
x_dense = np.linspace(min(x), max(x), 100)
y_dense = cs(x_dense)

plt.plot(x, y, 'o', label="Given Data Points")
plt.plot(x_dense, y_dense, '-', label="Cubic Spline Curve")
plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
