import numpy as np
import math

def cholesky(A):
    n = len(A)
    L = np.identity(n)

    L[0, 0] = math.sqrt(A[0, 0])

    for i in range(1, n):
        L[i, 0] = A[0, i] / L[0, 0]

    for i in range(1, n):
        L[i, i] = math.sqrt(A[i, i] - np.dot(L[i, 0:i], L[i, 0:i].T))
        for j in range(i + 1, n):
            L[j, i] = (A[i, j] - np.dot(L[i, 0:j], L[j, 0:j])) / L[i, i]

    return L, L.T