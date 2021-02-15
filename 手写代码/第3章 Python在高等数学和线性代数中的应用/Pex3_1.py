from sympy import *
x,y,z=symbols('x y z')
m0,m1,m2,m3=symbols('m0:4')
x=sin(1)
print("x=",x);print("x=",x.evalf())
print("x=",x.n(16))
print("pi的两种显示格式:{},{}".format(pi,pi.evalf(3)))
expr1=y*sin(y**2)
expr2=y**2+sin(y)*cos(y)+sin(z)
print("expr1=",expr1)
print("y=5时，expr1=",expr1.subs(y,5))
print("y=2,z=3时，expr2=",expr2.subs({y:2,z:3}))
print("y=2,z=3时,expr2",expr2.subs({y:2,z:3}).n())
