import numpy as np
a=np.linspace(0,2,5)
b=np.mgrid[0:5:5j]
print(a)
print(b)
x,y=np.mgrid[0:2:4j,10:20:5j]
print("x={}\ny={}".format(x,y))
print("X",x)