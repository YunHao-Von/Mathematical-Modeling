import numpy as np
a=np.arange(6).reshape(2,3)
a.tofile("Pdata2_22.bin")
b=np.fromfile("Pdata2_22.bin",dtype=int).reshape(2,3)
print(b)