import numpy as np
import math


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

def solve_system(A, b):
	L, D, L_t = LDL_t(A)
	y = forward_substitution(L, b)
	x = backward_substitution(np.dot(D, L_t), y)
	return x

A = np.array([[4.,-1.,1.],[-1.,3.,0.],[1.,0.,2.]])
b = np.array([-1.,4.,5.])
print('8a \n Solution: ' + str(solve_system(A, b)))
A = np.array([[4.,2.,2.],[2.,6.,2.],[2.,2.,5.]])
b = np.array([0.,1.,0.])
print('8b \n Solution: ' + str(solve_system(A, b)))
A = np.array([[4.,0.,2.,1.],[0.,3.,-1.,1.],[2.,-1.,6.,3.],[1.,1.,3.,8.]])
b = np.array([-2.,0.,7.,-2.])
print('8c \n Solution: ' + str(solve_system(A, b)))
A = np.array([[4.,1.,1.,1.],[1.,3.,0.,-1.],[1.,0.,2.,1.],[1.,-1.,1.,4.]])
b = np.array([2.,2.,1.,1.])
print('8d \n Solution: ' + str(solve_system(A, b)))
