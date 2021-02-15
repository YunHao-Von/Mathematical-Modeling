from sympy.plotting import plot
from sympy.abc import x,pi
from sympy.functions import sin,cos
plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)))