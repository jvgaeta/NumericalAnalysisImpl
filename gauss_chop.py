import numpy as np
import math

# Author: Jordan Gaeta

# How to run: Type 'python alg_6.2_10.py' from command line, python must be installed
# you also must have numpy have installed

# indices work differently here than in matlab so 
# the arrays start at 0 and end at n - 1
# so indexing at n is the same as indexing at n + 1
# also i take the input as already being augmented
# so the length is effectively n+1 even though it may not
# look like it

# this method performs the chopping that we want
# ex chop(1.9233, 3) --> math.floor(1.9233 * 10 ** 2) / 10 ** 2 ---> math.floor(192.33) / 100 ---> 192 / 100 --> 1.92
def chop(number, places):
    # loop to count the number places before decimal
    whole_number = int(math.floor(abs(number)))
    pre_decimal_count = 0
    while whole_number > 0:
        whole_number = whole_number / 10
        pre_decimal_count += 1
    if number >= 0:
        return math.floor(number * 10 ** (places - pre_decimal_count)) / (10 ** (places - pre_decimal_count))
    else:
        return math.ceil(number * 10 ** (places - pre_decimal_count)) / (10 ** (places - pre_decimal_count))

# we use this after vector operations as to chop vector operations
def chop_vec(v, places):
    temp = []
    for i in range(len(v)):
        temp.append(chop(v[i], places))
    return temp

# this performs backwards substitution
def backward_substitution(A):
    n = len(A)
    x = np.zeros(n) # create an array to hold the solutions
    i = n - 1
    x[i] = chop(A[i, -1] / A[i, i], 3)
    # loop to find all of the solutions, using backwards substitution
    for k in range(n - 2, -1, -1):
        # this obtains the last element in the row --> b_i
        summation = A[k, -1]
        for j in range(k + 1, n):
            summation = chop(summation - chop(A[k, j] * x[j], 3), 3)
        x[k] = chop(summation / A[k, k], 3)
    return x


# this function takes an augmented matrix and performs gaussian elimination
def gaussian_elimination(A):
    # size of the matrix
    n = len(A)

    # first loop
    for i in range(0, n - 1):

        p = i
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
            A[j] = A[j] - chop_vec(chop(A[j, i] / A[i, i], 3) * A[i], 3)
            A[j] = chop_vec(A[j], 3)
        print(A)

    if A[n - 1, n - 1] == 0:
        print('No unique solution!')
        return
    else:
        return backward_substitution(A)