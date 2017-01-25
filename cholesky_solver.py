import numpy as np
import math

def cholesky_solver(A, b):
	n = len(A)
	L = np.identity(n)

	L[0, 0] = math.sqrt(A[0, 0])

	for i in range(1, n):
		L[i, 0] = A[0, i] / L[0, 0]

	for i in range(1, n):
		L[i, i] = math.sqrt(A[i, i] - np.dot(L[i, 0:i], L[i, 0:i].T))
		for j in range(i + 1, n):
			L[j, i] = (A[i, j] - np.dot(L[i, 0:j], L[j, 0:j])) / L[i, i]

	y = np.zeros(n)
	y[0] = b[0] / L[0, 0]
	for i in range(1, n):
		y[i] = (b[i] - np.dot(L[i, 0:i], y[0:i])) / L[i, i]
	print(y)
	x = np.zeros(n)
	x[n - 1] = y[n - 1] / L[n - 1, n - 1]

	for i in range(n - 2, -1, -1):
		x[i] = (y[i] - np.dot(L[i:n, i], x[i:n])) / L[i, i]
	return x


A = np.array([[4.,-1.,1.],[-1.,3.,0.],[1.,0.,2.]])
a = np.array([-1.,4.,5.])
B = np.array([[4.,2.,2.],[2.,6.,2.],[2.,2.,5.]])
b = np.array([0.,1.,0.])
C = np.array([[4.,0.,2.,1.],[0.,3.,-1.,1.],[2.,-1.,6.,3.],[1.,1.,3.,8.]])
c = np.array([-2.,0.,7.,-2.])
D = np.array([[4.,1.,1.,1.],[1.,3.,0.,-1.],[1.,0.,2.,1.],[1.,-1.,1.,4.]])
d = np.array([2.,2.,1.,1.])
solution = cholesky_solver(A, a)
print('10a\nSolution: ' + str(solution))
solution = cholesky_solver(B, b)
print('10b\nSolution: ' + str(solution))
solution = cholesky_solver(C, c)
print('10c\nSolution: ' + str(solution))
solution = cholesky_solver(D, d)
print('10d\nSolution: ' + str(solution))