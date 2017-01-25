import numpy as np
import matplotlib.pyplot as plt

def PLS(x, y, n):
	mat = np.zeros((n + 1, n + 1))
	col = np.zeros(n + 1)
	for i in range(0, n + 1):
		for j in range(0, n + 1):
			col[i] = sum(y * (x ** i))
			mat[i, j] = sum(x**(i + j))
	return np.linalg.solve(mat, col)

def get_error(x, y, coeff):
	error = 0
	for i in range(0, len(y)):
		error += (y[i] - np.polyval(coeff, x[i]))**2
	return error

x = np.array([0,0.15,0.31,0.5,0.6,0.75])
y = np.array([1.0,1.004,1.031,1.117,1.223,1.422])
linear = PLS(x, y, 1)
square = PLS(x, y, 2)
cube = PLS(x, y, 3)
print('Solution PLS 1: ' + str(linear) + '\nError: ' + str(get_error(x, y, linear[::-1])))
print('Solution PLS 2: ' + str(square) + '\nError: ' + str(get_error(x, y, square[::-1])))
print('Solution PLS 3: ' + str(cube)) + '\nError: ' + str(get_error(x, y, cube[::-1]))

x_new = np.linspace(x[0], x[-1], num=len(x)*10)
fit_linear = np.polyval(linear[::-1], x_new)
fit_square = np.polyval(square[::-1], x_new)
fit_cube = np.polyval(cube[::-1], x_new)
choice = int(raw_input("Please enter the degree of the polynomial that you would like to graph: "))
if choice == 1:
	plt.plot(x_new, fit_linear)
elif choice == 2:
	plt.plot(x_new, fit_square)
elif choice == 3:
	plt.plot(x_new, fit_cube)
else:
	print('Currently Not Implemented.')
plt.plot(x, y)
plt.show()