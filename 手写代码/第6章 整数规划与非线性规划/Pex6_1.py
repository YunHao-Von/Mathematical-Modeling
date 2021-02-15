import cvxpy as cp
from numpy import array

c = array([40, 90])
a = array([
    [9, 7],
    [-7, -20]
])
b = array([56, -70])
x = cp.Variable(2, integer=True)
obj = cp.Minimize(c * x)
cons = [a * x <= b,
        x >= 0]
prob = cp.Problem(obj, cons)
prob.solve(solver='GLPK_MI', verbose=True)
print("最优值为：", prob.value)
print("最优解为：\n", x.value)
