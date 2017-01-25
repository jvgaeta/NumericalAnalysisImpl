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

A = np.array([[4.,-1.,1.],[-1.,3.,0.],[1.,0.,2.]])
B = np.array([[4.,2.,2.],[2.,6.,2.],[2.,2.,5.]])
C = np.array([[4.,0.,2.,1.],[0.,3.,-1.,1.],[2.,-1.,6.,3.],[1.,1.,3.,8.]])
D = np.array([[4.,1.,1.,1.],[1.,3.,0.,-1.],[1.,0.,2.,1.],[1.,-1.,1.,4.]])
L, L_t = cholesky(A)
print('6a\n\n L: \n' + str(L) + '\n\nL.t\n' + str(L_t) +'\n')
L, L_t = cholesky(B)
print('6b\n\n L: \n' + str(L) + '\n\nL.t\n' + str(L_t) +'\n')
L, L_t = cholesky(C)
print('6c\n\n L: \n' + str(L) + '\n\nL.t\n' + str(L_t) +'\n')
L, L_t = cholesky(D)
print('6d\n\n L: \n' + str(L) + '\n\nL.t\n' + str(L_t) +'\n')