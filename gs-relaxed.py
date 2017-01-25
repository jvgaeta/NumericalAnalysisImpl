import numpy as np

def gauss_seidel_relaxed(A, b):
    tolerance = 10**-20
    n = len(A)
    x = np.zeros(n)
    x1 = np.ones(n)
    w = 1.3
    iterations = 0
    while abs(x - x1).max() > tolerance and iterations < 2:
        x1 = np.copy(x)
        for i in range(0, n):
            x[i] = (1 - w)*x[i] + w * (b[i] - np.dot(A[i,0:i], x[0:i]) - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]
        print('Iteration ' + str(iterations + 1) +': ' + str(x))
        iterations += 1
    return x