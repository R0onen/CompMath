import numpy as np
import pandas as pd

A = np.array([[4, -1, 0],
              [-1, 4, -1],
              [0, -1, 4]], dtype=float)
b = np.array([15, 10, 10], dtype=float)

x0 = np.zeros_like(b)
def relaxation_method(A, b, x0, w, tol=1e-5, max_iter=100):
    x = x0
    n = len(b)
    history = []
    for _ in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            x_new[i] = (1 - w) * x[i] + (w / A[i, i]) * (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i+1:], x[i+1:]))
        history.append(x_new)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x_new, history

solution_1, history_1 = relaxation_method(A, b, x0, w=1.1)
solution_2, history_2 = relaxation_method(A, b, x0, w=1.5)

print("\nSolution for w=1.1:")
print(solution_1)
print("\nSolution for w=1.5:")
print(solution_2)
