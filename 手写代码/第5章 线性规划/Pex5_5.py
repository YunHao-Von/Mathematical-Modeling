import numpy
from cvxopt import matrix, solvers

c = matrix([2, 1])
A = matrix([
    [-1., 1],
    [-1, -1],
    [1, -2],
    [0, -1]
]).T
b = matrix([1., -2, 4, 0])
aeq = matrix([1., 2], (1, 2))
beq = matrix([3.5])
sol = solvers.lp(c, A, b, aeq, beq)
print(sol['x'])
print(sol['primal objective'])