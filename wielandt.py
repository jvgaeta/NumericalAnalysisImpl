import numpy as np
import eigenvalues as pm

def get_smallest_i(x):
	l = np.linalg.norm(x, ord=np.inf)
	for i in range(len(x)):
		if abs(x[i]) == l:
			return i


def wielandt(A, eigenvalue, v, x0, tol=.0001, N=1000):
	B = np.zeros((A.shape[0], A.shape[1]))
	n = A.shape[0]
	# step 1
	i = get_smallest_i(v)
	# step 2
	if i != 0:
		for k in range(0, i - 1):
			for j in range(0, i - 1):
				B[k, j] = A[k, j] - (v[k] / v[i]) * A[i, j]
	# step 3
	if i != 0 and i != n - 1:
		for k in range(0, i - 1):
			for j in range(0, i - 1):
				B[k, j] = A[k + 1, j] - (v[k + 1] / v[i]) * A[i, j]
				B[j, k] = A[j, k + 1] - (v[j] / v[i]) * A[i, k + 1]
	# step 4
	if i != n - 1:
		for k in range(i, n):
			for j in range(i, n):
				B[k, j] = A[k + 1, j + 1] - (v[k + 1] / v[i]) * A[i, j + 1]
	# step 5, 6
	B_prime = np.delete(np.delete(B, i, 0), i, 1)
	mu, w_prime = pm.power_method(B_prime, x0)
	# step 7
	w = np.zeros(len(w_prime) + 1)
	if i != 1:
		for k in range(0, i - 1):
			w[k] = w_prime[k]
	# step 8
	w[i] = 0
	# step 9
	if i != n:
		for k in range(i, n):
			w[k] = w_prime[k - 1]
	# step 10
	u = np.zeros(n)
	for k in range(0, n):
		u[k] = (mu - eigenvalue) * w[k] + np.dot(A, w.T) * (v[k] / v[i])

	return mu, u

A = np.array([[4., -1., 1.], [-1., 3., -2.], [1., -2., 3.]])
x = np.array([1., 0.])
print(wielandt(A, 6, np.array([1., -1., 1.]), x))

