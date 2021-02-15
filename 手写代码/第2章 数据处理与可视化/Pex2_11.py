import numpy as np
a=np.arange(4).reshape(2,2)
b=np.arange(4).reshape(2,2)
c=np.arange(4).reshape(2,2)
print(a.reshape(-1))
print(b.ravel())
print(c.flatten())