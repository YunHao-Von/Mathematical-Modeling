import numpy as np
a=np.arange(4).reshape(2,2)
b=np.arange(4,8).reshape(2,2)
c1=np.vstack([a,b])
c2=np.r_[a,b]
d1=np.hstack([a,b])
d2=np.c_[a,b]
print(c1)
print(c2)
print(d1)