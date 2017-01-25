import numpy as np

def cgd(A, b, maxIter):
    n = len(b)
    x = np.zeros(len(b))
    r = b - np.dot(A, x)
    v = r
    for k in range(0, maxIter):
        t = np.dot(r, r) / np.dot(v, np.dot(A, v))
        x = x + t * v
        r1 = r - t * np.dot(A, v)
        s = np.dot(r1, r1) / np.dot(r, r)
        v = r1 + s * v
        r = r1
    return x

# builds the desired matrices for the problem
def build_matrix(n):
    A = np.zeros((n - 1, n - 1))
    b = np.zeros(n - 1)
    b[0] = 1./2.
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if i == j:
                A[i, j] = 1.0
            elif (i == j + 1) or (j == i + 1):
                A[i, j] = -1./2.
    return A, b

m1, b1 = build_matrix(10)
m2, b2 = build_matrix(50)
m3, b3 = build_matrix(100)