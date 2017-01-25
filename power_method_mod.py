import numpy as np
import gauss_pp as slvr

def get_smallest_p(x):
	l = np.linalg.norm(x, ord=np.inf)
	for i in range(len(x)):
		if abs(x[i]) == l:
			return i

def power_method(A, x0, tol=.000001, N=10000):
	q = np.dot(np.dot(x0.T, A), x0) / np.dot(x0.T, x0)
	p = get_smallest_p(x0)
	x = x0 / x0[p]
	for k in range(1, N + 1):
		lhs = A - q * np.identity(len(A))
		mat = np.column_stack((lhs, x))
		y = slvr.gaussian_elimination(mat)
		mu = y[p]
		p = get_smallest_p(y)
		error = np.linalg.norm((x - (y / y[p])), ord=np.inf)
		x = y / y[p]
		if error < tol:
			return 1 / mu + q, x
	return 1 / mu + q, x

A1 = np.array([[-4.,14.,0.], [-5.,13.,0.], [-1.,0.,2.]])
x1 = np.array([1., 1., 1.])
print(power_method(A1, x1))