from sympy.abc import x
from sympy import diff, dsolve, simplify, Function
y=Function('y')
eq=diff(y(x),x,2)+2*diff(y(x),x)+2*y(x)
con={y(0):0,diff(y(x),x).subs(x,0):1}
y=dsolve(eq,ics=con)
print(simplify(y))