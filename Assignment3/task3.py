import numpy as np
import pandas as pd

def gauss_jordan(A, b):
    n = len(b)
    M = np.hstack((A, b.reshape(-1, 1)))

    for i in range(n):
        # Make diagonal 1
        M[i] /= M[i, i]
        for j in range(n):
            if i != j:
                M[j] -= M[j, i] * M[i]

    return M[:, -1], M

A = np.array([[2, 1, -1], 
              [-3, -1, 2], 
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

solution, diagonal_matrix = gauss_jordan(A, b)
print("\nDiagonal Matrix:")
print(diagonal_matrix)
print("\nSolution:")
print(solution)
