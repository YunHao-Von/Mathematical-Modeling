from sympy.abc import x
from sympy import Function, diff, dsolve, sin

y = Function('y')
eq = diff(y(x), x, 2) + 2 * diff(y(x), x) + 2 * y(x) - sin(x)
con = {y(0): 0, diff(y(x), x).subs(x, 0): 1}
y = dsolve(eq, ics=con)
print(y)
