import numpy as np
import pandas as pd

A = np.array([[8, -3, 2],
              [4, 11, -1],
              [6, 3, 12]], dtype=float)
b = np.array([20, 33, 36], dtype=float)

def gauss_seidel(A, b, x0, tol=1e-5, max_iter=100):
    x = x0
    n = len(b)
    history = []
    for _ in range(max_iter):
        x_new = np.copy(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        history.append(x_new)
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x_new, history

x0 = np.zeros_like(b)
solution, history = gauss_seidel(A, b, x0)

df = pd.DataFrame(history, columns=['x1', 'x2', 'x3'])
print("\nSolution:")
print(solution)
print("\nIterations Table:")
print(df)
