from numpy import  sin
from scipy.optimize import fsolve
def pfun(x):
    x1,x2,x3=x.tolist()
    return 5*x2+3,4*x1**2-2*sin(x2*x3),x2*x3-1.5
print("result=",fsolve(pfun,[1.0,1.0,1.0]))