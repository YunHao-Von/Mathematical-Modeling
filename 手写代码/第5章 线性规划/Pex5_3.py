from scipy.optimize import linprog
import numpy as np

c = np.array([-110, -120, -130, -110, -115, 150])
a = [
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [8.8, 6.1, 2.0, 4.2, 5.0, -6],
    [-8.8, -6.1, -2.0, -4.2, -5.0, 3]
]
b=[
    [200],[250],[0],[0]
]
aeq = [[1, 1, 1, 1, 1, -1]]
beq = [[0]]
LB = [0] * len(c)
UB = [None] * len(c)
bounds =tuple(zip(LB,UB))
res=linprog(-c,a,b,aeq,beq,bounds)
print(res.fun)
print(res.x)