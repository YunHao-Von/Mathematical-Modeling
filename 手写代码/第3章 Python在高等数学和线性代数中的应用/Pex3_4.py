from pylab import rc
from sympy.plotting import plot3d
from sympy.abc import x,y
from sympy.functions import sin,sqrt
rc('font',size=16);rc('text',usetex=False)
plot3d(sin(sqrt(x**2+y**2)),(x,-10,10),(y,-10,10),xlabel='$x$',ylabel='$y$')