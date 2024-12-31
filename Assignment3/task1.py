import numpy as np
import pandas as pd

# System of equations: Ax = b
A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)
b = np.array([15, 10, 10], dtype=float)

# Check diagonal dominance
is_diag_dominant = all(2 * abs(A[i, i]) > np.sum(abs(A[i, :])) for i in range(len(A)))
print("Diagonal dominance criterion satisfied:", is_diag_dominant)

# Jacobi method
def jacobi(A, b, x0, tol=1e-5, max_iter=100):
    D = np.diag(np.diag(A))
    R = A - D
    x = x0
    history = []
    for _ in range(max_iter):
        x_new = np.dot(np.linalg.inv(D), b - np.dot(R, x))
        history.append(x_new)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x_new, history

x0 = np.zeros_like(b)
solution, history = jacobi(A, b, x0)

# Display results
df = pd.DataFrame(history, columns=['x1', 'x2', 'x3'])
print("\nSolution:")
print(solution)
print("\nIterations Table:")
print(df)
