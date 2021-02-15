import numpy as np
a=np.loadtxt("Pdata2_20.txt",dtype=str,delimiter=",")
print(a)
b=a[1:,1:].astype(float)
print("b=",b)