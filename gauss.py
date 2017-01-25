import numpy as np
import math

# Author: Jordan Gaeta

# indices work differently here than in matlab so 
# the arrays start at 0 and end at n - 1
# so indexing at n is the same as indexing at n + 1
# also i take the input as already being augmented
# so the length is effectively n + 1 even though it may not
# look like it

# this performs backwards substitution
def backward_substitution(A):
    n = len(A)
    x = np.zeros(n) # create an array to hold the solutions
    i = n - 1
    print(A)
    x[i] = A[i, -1] / A[i, i]
    # loop to find all of the solutions, using backwards substitution
    for k in range(n - 2, -1, -1):
        # this obtains the last element in the row --> b_i
        summation = A[k, -1]
        for j in range(k + 1, n):
            summation -= A[k, j] * x[j]
        x[k] = summation / A[k, k]

    return x


# this function takes an augmented matrix and performs gaussian elimination
def gaussian_elimination(A):
    # size of the matrix
    n = len(A)

    # first loop
    for i in range(0, n - 1):

        # select pivot
        for pivot in range(i, n):

            if A[pivot, i] != 0: 
                p = pivot
                break

        # check to see if it worked
        if A[p, i] == 0:
            print('This is a singular matrix.')
            return

        # perform the swap here
        if p != i:
            A[[i, p]] = A[[p, i]]

        # second loop
        for j in range(i + 1, n):
            A[j] = A[j] - (A[j, i] / A[i, i]) * A[i]

    if A[n - 1, n - 1] == 0:
        print('No unique solution!')
        return
    else:
        return backward_substitution(A)
