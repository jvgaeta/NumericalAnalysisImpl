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

A = np.array([[4.,1.,-1.],[-1.,3.,1.],[2.,2.,5.]])
a = np.array([5.,-4.,1.])
B = np.array([[-2.,1.,1./2.],[1.,-2.,-1./2.],[0.,1.,2.]])
b = np.array([4.,-4.,0.])
C = np.array([[4.,1.,-1.,1.],[1.,4.,-1.,-1.],[-1.,-1.,5.,1.],[1.,-1.,1.,3.]])
c = np.array([-2.,-1.,0.,1.])
D = np.array([[4.,-1.,0.,0.,0.,0.],[-1.,4.,-1.,0.,0.,0.],[0.,-1.,4.,0.,0.,0.],
	[0.,0.,0.,4.,-1.,0.],[0.,0.,0.,-1.,4.,-1.],[0.,0.,0.,0.,-1.,4.]])
d = np.array([0.,5.,0,6.,-2.,6.])
print('4a')
gauss_seidel_relaxed(A, a)
print('\n4b')
gauss_seidel_relaxed(B, b)
print('\n4c')
gauss_seidel_relaxed(C, c)
print('\n4d')
gauss_seidel_relaxed(D, d)