import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [1, 2],
    [3, 4]
])
c=a+b
x=np.mod(c,2)
print(x)
