import numpy as np
import gauss_pp as slvr
from pylab import *
import matplotlib.pyplot  as pyplot

# F(x)
def F(x):
    return np.array([[x[0]**2 + x[1]**2 - 2], [x[0]**2 - x[1]**2 - 1]])

#compute the Jacobian
def J(x):
    return np.array([[2.0*x[0], 2.0*x[1]], [2.0*x[0], -2.0*x[1]]])

def Newton(x, tol=.0001, N=1000):
    k = 0
    while k <= N:
    	f = F(x)
    	j = J(x)
    	mat = np.column_stack((j, -1.0 * f))
    	y = slvr.gaussian_elimination(mat)
    	x = x + y
    	if np.linalg.norm(y, ord=np.inf) < tol:
    		return x
        k += 1
    return x

solution = Newton(np.array([1., 1.]))