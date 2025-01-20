import numpy as np
import pandas as pd

# Task 6: Backward Difference Table
x = np.array([5, 6, 7, 8, 9])
y = np.array([1, 8, 27, 64, 125])

# Compute backward difference table
n = len(y)
backward_diff = np.zeros((n, n))
backward_diff[:, 0] = y

for j in range(1, n):
    for i in range(j, n):
        backward_diff[i, j] = backward_diff[i, j - 1] - backward_diff[i - 1, j - 1]

# Display backward difference table
df_backward = pd.DataFrame(backward_diff, columns=[f"d^{i}y" for i in range(n)])
print("Task 6: Backward Difference Table")
print(df_backward)
