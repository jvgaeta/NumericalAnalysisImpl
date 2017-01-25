import numpy as np

# do it in matrix form ---> faster
def jacobi(A, b):
	tolerance = 10**-5
	n = len(A)
	x = np.zeros(n)
	x1 = np.ones(n)
	diag = np.diag(A)
	remaining = A - np.diagflat(diag)
	while abs(x - x1).max() > tolerance:
		x1 = np.copy(x)
		x = (b - np.dot(remaining, x)) / diag
		print(x)
	return x 

def gauss_seidel(A, b):
	tolerance = 10**-5
	n = len(A)
	x = np.zeros(n)
	x1 = np.ones(n)
	iterations = 0
	while abs(x - x1).max() > tolerance and iterations < 25:
		x1 = np.copy(x)
		for i in range(0, n):
			x[i] = (b[i] - np.dot(A[i,0:i], x[0:i]) - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]
		iterations += 1
		print(x)
	return x

A = np.array([[4.,1.,-1.],[-1.,3.,1.],[2.,2.,5.]])
b = np.array([5.,-4.,1.])
gauss_seidel(A, b)
