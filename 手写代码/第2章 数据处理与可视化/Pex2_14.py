import numpy as np
a=np.arange(10,15)
b=np.arange(5,10)
c=a+b;d=a*b
e1=np.modf(a/b)[0]
e2=np.modf(a/b)[1]
print(a)
print(b)
print(e1)
print(e2)