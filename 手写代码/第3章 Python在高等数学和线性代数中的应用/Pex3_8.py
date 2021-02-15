from sympy import *
k,n=symbols('k n')
print(summation(k**2,(k,1,n)))
print(factor(summation(k**2,(k,1,n))))
print(summation(1/k**2,(k,1,oo)))