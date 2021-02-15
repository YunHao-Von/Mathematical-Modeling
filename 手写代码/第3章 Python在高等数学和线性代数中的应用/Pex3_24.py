from numpy import exp,cos
from scipy.optimize import fmin
f=lambda x:exp(x)*cos(2*x)
x0=fmin(f,0)
print(x0)