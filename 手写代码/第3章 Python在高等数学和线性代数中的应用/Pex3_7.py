from sympy import *
x,y=symbols('x y')
z=sin(x)+x**2*exp(y)
print('z的一阶偏导数为:',diff(z,x,2))
print('z的二阶偏导数为:',diff(z,y))