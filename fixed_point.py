import math

def G(x):
    g1 = 1/10.0 * x[0]**2 - 1/10.0 * x[1]**2 - 4.0/5.0
    g2 = (x[0]*x[1]**2 + x[0] - 8.0) / 10.0
    return [g1, g2]


def fixed_point(x, N=10000):
    g = x
    for k in range(1, N + 1):
        g = G(x)
        x = g
    return g