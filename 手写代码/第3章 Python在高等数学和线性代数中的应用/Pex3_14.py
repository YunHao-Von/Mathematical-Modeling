from sympy import *
x=symbols('x');y=symbols('y',cls=Function)
eq1=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)
eq2=diff(y(x),x,2)-5*diff(y(x),x)+6*y(x)-x*exp(2*x)
print(dsolve(eq1,y(x)))
print(dsolve(eq2,y(x)))