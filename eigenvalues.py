import numpy as np

def get_smallest_p(x):
	l = np.linalg.norm(x, ord=np.inf)
	for i in range(len(x)):
		if abs(x[i]) == l:
			return i

def power_method(A, x0, tol=.01, N=100):
	p = get_smallest_p(x0)
	x = x0 / x0[p]
	for k in range(1, N + 1):
		y = np.dot(A, x)
		mu = y[p]
		p = get_smallest_p(y)
		if y[p] == 0:
			print('Error select a new vector x and restart')
			return
		error = np.linalg.norm((x - (y / y[p])), ord=np.inf)
		x = y / y[p]
		if error < tol:
			return mu, x
		print('Iteration: ' + str(k))
		print('Eigenvalue: ' + str(mu) + ' Eigenvector: ' + str(x))
	return mu, x
