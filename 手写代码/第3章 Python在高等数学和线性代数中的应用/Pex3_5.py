from pylab import rc
from sympy import plot_implicit as pt,Eq
from sympy.abc import x,y
rc('font',size=16);rc('text',usetex=False)
pt(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4),xlabel='$x$',ylabel='$y$')
from sympy import plot_implicit as pt
from sympy.abc import x,y
ezplot=lambda expr:pt(expr)
ezplot((x-1)**2+(y-2)**3-4)