from scipy.linalg import qr
import numpy as np
from scipy.linalg import lu
# Given matrix A
A = np.array([[4, 1, 2, 0],
              [1, 3, 1, 2],
              [2, 1, 5, 1],
              [0, 2, 1, 4]], dtype=float)

# Givens rotation
_, R_givens = qr(A, mode='economic')

# Householder reduction
Q_householder, R_householder = qr(A, mode='full')

print("\nMatrix R using Givens method:")
print(R_givens)

print("\nMatrix Q and R using Householder method:")
print(Q_householder)
print(R_householder)
