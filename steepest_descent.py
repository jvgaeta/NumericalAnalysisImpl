import numpy as np
import math

# This is the function
def f(x):
    return (3*x[0] - math.cos(x[0] * x[1]) - 1.0/2.0)**2 
    + (x[0]**2 - 81.0*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06)**2 
    + (math.exp(-x[0]*x[1]) + 20.0*x[2] + (10.0 * math.pi - 3.0)/3.0)**2

# compute gradient at a point
def gradient(x):
    grad1 = (4.0*x[0]*(x[0]**2 - 81.0*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06) 
        - 2*x[1]*math.exp(-x[0]*x[1])*(math.exp(-x[0]*x[1]) + 20.0*x[2] + (1.0/3.0)*(10.0*math.pi - 3.0)))
    + 2.0*(x[1]*math.sin(x[0]*x[1]) + 3.0)*(-math.cos(x[0]*x[1]) + 3*x[0] - 1.0/2.0)

    grad2 = -324.0*(x[1]+0.1)*(x[0]**2 - 81.0*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06) 
    - 2.0*x[0]*math.exp(-x[0]*x[1])*(math.exp(-x[0]*x[1]) + 20.0*x[2] + (1.0/3.0)*(10.0*math.pi - 3.0)) 
    + 2.0*x[0]*math.sin(x[0]*x[1])*(-math.cos(x[0]*x[1]) + 3.0*x[0] - 1.0/2.0)

    grad3 = 2.0*math.cos(x[2])*(x[0]**2 - 81.0*(x[1] + 0.1)**2 + math.sin(x[2]) + 1.06) 
    + 40.0*(math.exp(-x[0]*x[1]) + 20.0*x[2] + (1.0 / 3.0)*(10.0 * math.pi - 3.0))

    return np.array([grad1, grad2, grad3])

# backtracking line search algorithm
def line_search(vector):
    alpha = 1.0
    f1 = f(vector)
    print gradient(vector)
    f2 = f(vector - alpha*gradient(vector))
    while f2 > f1:
        f2 = f(vector - alpha*gradient(vector))
        alpha = alpha / 2.0
    return alpha

#perform gradient descent
def gradient_descent(x, tol=.000001):
    err = float("inf") # start error at infinity
    while abs(max(x - err)) > tol:
        err = x # update error
        alpha = line_search(x) # compute alpha using line search algo
        x = x - alpha*gradient(x) # descend
    return x

x = np.array([0.0, 0.0, 0.0])
print(gradient_descent(x))