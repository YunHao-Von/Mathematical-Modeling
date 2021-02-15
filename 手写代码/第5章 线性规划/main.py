import numpy
from cvxopt import matrix, solvers


A = matrix([
    [-1., 1],
    [-1, -1],
    [1, -2],
    [0, -1]
]).T
print(A)
A = matrix([
    [-1, 1],
    [-1, -1],
    [1, -2],
    [0, -1]
]).T
print(A)