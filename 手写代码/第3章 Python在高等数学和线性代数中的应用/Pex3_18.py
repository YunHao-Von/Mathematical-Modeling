import numpy as np
from scipy.integrate import quad
def trapezoid(f,n,a,b):
    xi=np.linspace(a,b,n)
    h=(b-a)/(n-1)
    return h*(np.sum(f(xi))-(f(a)+f(b))/2)
def simpson(f,n,a,b):
    xi,h=np.linspace(a,b,2*n+1),(b-a)/(2.0*n)
    xe = [f(xi[i]) for i in range(len(xi)) if i%2==0]
    x0 = [f(xi[i]) for i in range(len(xi)) if i % 2 != 0]
    return h*(2*np.sum(xe)+4*np.sum(x0)-f(a)-f(b))/3.0
a=0;b=1;n=1000
f=lambda x:np.sin(np.sqrt(np.cos(x)+x**2))
print(trapezoid(f,n,a,b))
print(simpson(f,n,a,b))
print(quad(f,a,b))