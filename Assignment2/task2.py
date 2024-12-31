import numpy as np
from scipy.linalg import lu

# Given matrix A and vector b
A = np.array([[2, 1, 1],
              [4, -6, 0],
              [-2, 7, 2]], dtype=float)
b = np.array([5, -2, 9], dtype=float)

# LU Decomposition
P, L, U = lu(A)

print("Permutation matrix P:")
print(P)
print("\nLower triangular matrix L:")
print(L)
print("\nUpper triangular matrix U:")
print(U)

# Solving Ly = Pb
Pb = np.dot(P, b)
y = np.linalg.solve(L, Pb)

# Solving Ux = y
x = np.linalg.solve(U, y)

print("\nSolution vector x:")
print(x)

# Compare with numpy.linalg.solve
x_np = np.linalg.solve(A, b)
print("\nSolution using numpy.linalg.solve:")
print(x_np)

# Verification
assert np.allclose(x, x_np), "Solutions do not match!"
