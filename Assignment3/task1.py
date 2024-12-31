import numpy as np
import matplotlib.pyplot as plt

# Task 1: Iterative Matrix Inversion

def iterative_matrix_inversion(A, tol=1e-6, max_iter=100):
    """Computes the inverse of matrix A iteratively."""
    n = A.shape[0]
    trace = np.trace(A)
    B = np.eye(n) / trace  # Initial guess B = (1/tr(A)) * I
    I = np.eye(n)  # Identity matrix

    for k in range(max_iter):
        R = I - np.dot(A, B)
        B_new = B + np.dot(B, R)

        # Convergence check
        if np.linalg.norm(R, ord=np.inf) < tol:
            return B_new, k + 1  # Return inverse and iterations

        B = B_new

    raise ValueError("Iterative method did not converge within max_iter steps.")

# Given matrix
A = np.array([
    [5, 2, 1],
    [2, 6, 3],
    [1, 3, 7]
], dtype=float)

# Compute inverse iteratively
try:
    B_iterative, iterations = iterative_matrix_inversion(A)
    print("Iterative Inverse Matrix:")
    print(B_iterative)
    print(f"Converged in {iterations} iterations.")
except ValueError as e:
    print(e)

# Compare with numpy.linalg.inv
B_numpy = np.linalg.inv(A)
print("\nNumpy Inverse Matrix:")
print(B_numpy)

# Error comparison
error = np.linalg.norm(B_iterative - B_numpy, ord=np.inf)
print(f"\nError between iterative and numpy inverse: {error:.6e}")

# Visualization of Convergence (optional)
def convergence_analysis(A, tol=1e-6, max_iter=100):
    trace = np.trace(A)
    B = np.eye(A.shape[0]) / trace
    I = np.eye(A.shape[0])
    errors = []

    for k in range(max_iter):
        R = I - np.dot(A, B)
        errors.append(np.linalg.norm(R, ord=np.inf))
        if errors[-1] < tol:
            break
        B = B + np.dot(B, R)

    return errors

errors = convergence_analysis(A)
plt.figure(figsize=(8, 6))
plt.semilogy(errors, marker='o', label="Residual Norm")
plt.title("Convergence Analysis of Iterative Matrix Inversion")
plt.xlabel("Iteration")
plt.ylabel("Residual Norm (log scale)")
plt.grid()
plt.legend()
plt.show()