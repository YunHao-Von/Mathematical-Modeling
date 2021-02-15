from numpy import exp,cos
from scipy.optimize import fminbound
f=lambda x:exp(x)*cos(2*x)
x0=fminbound(f,0,3)
print(x0)