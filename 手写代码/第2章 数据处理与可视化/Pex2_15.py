import numpy as np
a=np.array([[3,4,9],[12,15,1]])
b=np.array([[2,6,3],[7,8,12]])
print(a[a>b])
print(a[a>10])
print(np.where(a>10,-1,a))
print(np.where(a>10,-1,0))