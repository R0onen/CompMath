import numpy as np
import pandas as pd

# Task 7: Higher-Order Differences
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 8, 27, 64, 125])

# Compute forward differences up to the fourth order
n = len(y)
higher_diff = np.zeros((n, n))
higher_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        higher_diff[i, j] = higher_diff[i + 1, j - 1] - higher_diff[i, j - 1]

# Display the fourth forward difference
fourth_forward_diff = higher_diff[0, 4]
print("Task 7: Higher-Order Forward Differences")
print(pd.DataFrame(higher_diff, columns=[f"d^{i}y" for i in range(n)]))
print(f"Fourth Forward Difference: {fourth_forward_diff}")
