import numpy as np
import eigenvalues as pm

def get_smallest_i(x):
	l = np.linalg.norm(x, ord=np.inf)
	for i in range(len(x)):
		if abs(x[i]) == l:
			return i

def householder(A, eigenvalue, v, x, tol=.00001, N=100):
	B = np.zeros((A.shape[0], A.shape[1]))
	# step 1
	i = get_smallest_i(v)
	# step 2
	if i != 0:
		for k in range(0, i):
			for j in range(0, i):
				B[k, j] = A[k, j] - (v[k] / v[i]) * A[i, j]

	# step 3
	if i != 0 and i != n - 1:
		for k in range(i, n):
			for j in range(0, i):
				B[k, j] = A[k + 1, j] - (v[k + 1] / v[i]) * A[i, j]
				B[j, k] = A[j, k + 1] - (v[j] / v[i]) * A[i, k + 1]
	# step 4
	if i != n - 1:
		for k in range(i, n):
			for j in range(i, n):
				B[k, j] = A[k + 1, j + 1] - (v[k + 1] / v[i]) * A[i, j + 1]
	# step 5





