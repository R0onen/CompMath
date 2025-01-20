import numpy as np
import pandas as pd

# Task 5: Forward Difference Table
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 7, 13, 21])

# Compute forward difference table
n = len(y)
forward_diff = np.zeros((n, n))
forward_diff[:, 0] = y

for j in range(1, n):
    for i in range(n - j):
        forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

# Display forward difference table
df_forward = pd.DataFrame(forward_diff, columns=[f"d^{i}y" for i in range(n)])
print("Task 5: Forward Difference Table")
print(df_forward)
