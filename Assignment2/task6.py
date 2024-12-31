import numpy as np
import pandas as pd

A = np.array([[1, 1.01], 
              [1.01, 1]], dtype=float)
b = np.array([2, 2.01], dtype=float)

# Analytical solution
x_analytical = np.linalg.solve(A, b)

# Numerical perturbation
b_perturbed = b + np.array([0.01, -0.01])
x_numerical = np.linalg.solve(A, b_perturbed)

print("\nAnalytical Solution:")
print(x_analytical)
print("\nPerturbed Numerical Solution:")
print(x_numerical)
