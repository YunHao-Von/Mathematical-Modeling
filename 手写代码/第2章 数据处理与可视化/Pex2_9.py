import numpy as np
x=np.array([[1,2],[3,4],[5,6]])
x[2,0]=1
y=np.delete(x,2,axis=0)
z=np.delete(y,0,axis=1)
t1=np.append(x,[[7,8]],axis=0)
t2=np.append(x,[[9],[10],[11]],axis=1)
print(x)
print(y)
print(z)
print(t1)
print(t2)