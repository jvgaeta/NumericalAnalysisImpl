import numpy as np
import math

def vec_sum_squares(L, D, i):
    total = 0
    for j in range(i):
        total += (L[i, j]**2) * D[j, j]
    return total

def vec_sum(L, D, j, i):
    total = 0
    for k in range(j):
        total += L[j, k] * L[i, k] * D[k, k]
    return total

def LDL_t(A):
    n = len(A)
    L = np.identity(n)
    D = np.diag(np.diag(L))

    for i in range(n):
        D[i, i] = A[i, i] - vec_sum_squares(L, D, i)

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - vec_sum(L, D, i, j)) / D[i, i]

    return L, D, L.T