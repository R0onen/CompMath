import numpy as np
import pandas as pd
def gaussian_with_pivot(A, b):
    n = len(b)
    M = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        # Pivoting
        max_row = max(range(i, n), key=lambda r: abs(M[r, i]))
        M[[i, max_row]] = M[[max_row, i]]

        # Elimination
        for j in range(i + 1, n):
            factor = M[j, i] / M[i, i]
            M[j, i:] -= factor * M[i, i:]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i + 1:-1], x[i + 1:])) / M[i, i]
    return x, M

A = np.array([[2, 3, 1], 
              [4, 11, -1], 
              [-2, 1, 7]], dtype=float)
b = np.array([10, 33, 15], dtype=float)

solution, upper_triangular = gaussian_with_pivot(A, b)
print("\nUpper Triangular Matrix:")
print(upper_triangular)
print("\nSolution:")
print(solution)
