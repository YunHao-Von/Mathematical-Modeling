from scipy.optimize import minimize
from numpy import ones


def obj(x):
    x1, x2, x3 = x
    return (2 + x1) / (1 + x2) - 3 * x1 + 4 * x3


LB = [0.1] * 3
UB = [0.9] * 3
bounds = tuple(zip(LB, UB))
res = minimize(obj, ones(3), bounds=bounds)  # ones(3)这里代表着初值
print(res.fun)
print(res.success, '\n', res.x)
