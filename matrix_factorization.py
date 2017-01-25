import numpy as np
import math

# Author: Jordan Gaeta

def backward_substitution(U, y):
    n = len(U)
    x = np.zeros(n) # create an array to hold the solutions
    k = n - 1
    x[k] = y[k] / U[k, k]
    # loop to find all of the solutions, using backwards substitution
    for i in range(n - 2, -1, -1):
        # this obtains the last element in the row --> b_i
        summation = y[i]
        for j in range(i + 1, n):
            summation -= U[i, j] * x[j]
        x[i] = summation / U[i, i]
    return x

def forward_substitution(L, b):
    y = np.zeros(len(L))
    y[0] = b[0] / L[0, 0]
    for i in range(1, len(L)):
        summation = b[i]
        for j in range(i):
            summation -= L[i, j] * y[j]
        y[i] = summation / L[i, i]
    return y


# this function does the matrix factorization
def myLU(A, b):
    U = A
    n = len(A)
    L = np.identity(n)
    # P = np.identity(n)
    i = 0
    for k in range(n - 1):
        for pivot in range(k, n):
            if A[pivot, i] != 0:
                i = pivot
                break
        #if i != k:
        #   U[[k, i], k:n] = U[[i, k], k:n]
        #   L[[k, i], 1:k-1] = L[[i, k], 1:k-1]
        #   P[[k, i], :] = P[[i, k], :]
        for i in range(k + 1, n):
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:n] = U[i, k:n] - np.dot(L[i, k], U[k, k:n])

    return L, U

def solve_system(A, b):
    L, U = myLU(A, b)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

