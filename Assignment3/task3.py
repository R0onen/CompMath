import numpy as np
from scipy.linalg import lu
# Power Iteration for the largest eigenvalue and eigenvector
def power_method(A, v0, tol=1e-6, max_iter=1000):
    v = v0 / np.linalg.norm(v0)
    for i in range(max_iter):
        w = np.dot(A, v)
        lambda_new = np.dot(v.T, w)
        v_new = w / np.linalg.norm(w)
        if np.linalg.norm(v_new - v) < tol:
            return lambda_new, v_new
        v = v_new
    raise ValueError("Power method did not converge")

A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]], dtype=float)

v0 = np.array([1, 0, 0], dtype=float)
largest_eigenvalue, largest_eigenvector = power_method(A, v0)

print("\nLargest Eigenvalue:")
print(largest_eigenvalue)
print("\nCorresponding Eigenvector:")
print(largest_eigenvector)

# Compare with numpy.linalg.eig
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues using numpy:")
print(eigvals)
print("\nEigenvectors using numpy:")
print(eigvecs[:, np.argmax(eigvals)])
