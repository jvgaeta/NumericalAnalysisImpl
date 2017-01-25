import numpy as np

def OLS(X, y):
	w = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
	return w

def OLS2(x, y):
	n = len(x)
	a = (n * np.dot(x, y.T) - sum(x) * sum(y)) / (n * sum(x**2) - sum(x)**2)
	b = (sum(x**2) * sum(y) - np.dot(x, y.T) * sum(x)) / (n * sum(x ** 2) - sum(x)**2)
	return a, b

def PLS(x, y, n):
	mat = np.zeros((n + 1, n + 1))
	col = np.zeros(n + 1)
	for i in range(0, n + 1):
		for j in range(0, n + 1):
			col[i] = sum(y * (x ** i))
			mat[i, j] = sum(x**(i + j))
	return np.linalg.solve(mat, col)


print('Solution OLS (a, b): ' + str(OLS2(np.array([1.,2.,3.,4.,5.]), np.array([3.,4.,9.,8.,11.]))))

print('Solution PLS: ' + str(PLS(np.array([0,0.15,0.31,0.5,0.6,0.75]), np.array([1.0,1.004,1.031,1.117,1.223,1.422]), 2)))