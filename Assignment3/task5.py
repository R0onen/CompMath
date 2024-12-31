import numpy as np
from scipy.linalg import lu
def jacobi_eigenvalue_method(A, tol=1e-6, max_iter=100):
    n = A.shape[0]
    V = np.eye(n)
    for _ in range(max_iter):
        i, j = np.unravel_index(np.argmax(np.abs(np.triu(A, 1))), A.shape)
        if np.abs(A[i, j]) < tol:
            break
        phi = 0.5 * np.arctan2(2 * A[i, j], A[j, j] - A[i, i])
        R = np.eye(n)
        R[i, i] = R[j, j] = np.cos(phi)
        R[i, j] = -np.sin(phi)
        R[j, i] = np.sin(phi)
        A = R.T @ A @ R
        V = V @ R
    return np.diag(A), V

A = np.array([[1, 1, 0.5],
              [1, 1, 0.25],
              [0.5, 0.25, 2]], dtype=float)

eigenvalues, eigenvectors = jacobi_eigenvalue_method(A)

print("\nEigenvalues using Jacobi's method:")
print(eigenvalues)

# Compare with numpy.linalg.eigvals
eigvals_np = np.linalg.eigvals(A)
print("\nEigenvalues using numpy:")
print(eigvals_np)
