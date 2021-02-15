from sympy import *
x,y=symbols('x y')
print(solve(x**3-1,x))
print(solve((x-2)**2*(x-1)**3,x))
print(roots((x-2)**2*(x-1)**3,x))