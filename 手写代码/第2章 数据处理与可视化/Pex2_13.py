import numpy as np
a=np.arange(4).reshape(2,2)
b=np.hsplit(a,2)
c=np.vsplit(a,2)
print(a)
print(b[0].shape)
print(c[0].shape)