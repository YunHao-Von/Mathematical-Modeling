from scipy.optimize import linprog

c = [-1, 2, 3]
A = [
    [-2, 1, 1],
    [3, -1, -2]
]
B = [
    [9],
    [-4]
]
Aeq = [
    [4, -2, -1]
]
beq = [-6]
LB = [-10, 0, None]
UB = [None] * len(c)
bounds = tuple(zip(LB, UB))
res=linprog(c,A,B,Aeq,beq,bounds)
print(res.fun)
print(res.x)