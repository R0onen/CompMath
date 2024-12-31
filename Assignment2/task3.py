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

A = np.array([[1, 1, 1], 
              [2, -3, 4], 
              [3, 4, 5]], dtype=float)
b = np.array([9, 13, 40], dtype=float)

solution, diagonal_matrix = gauss_jordan(A, b)
print("\nDiagonal Matrix:")
print(diagonal_matrix)
print("\nSolution:")
print(solution)
