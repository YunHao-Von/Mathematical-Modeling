import numpy as np
a=np.arange(0,3,0.5).reshape(2,3)
np.savetxt("Pdata2_18_1.txt",a)
b=np.loadtxt("Pdata2_18_1.txt")
print("b=",b)
np.savetxt("Pdata2_18_2.txt",a,fmt="%d",delimiter=",")
c=np.loadtxt("Pdata2_18_2.txt",delimiter=",")
print("c=",c)