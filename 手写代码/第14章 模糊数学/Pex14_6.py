import numpy as np

a = np.array([0.3, 0.35, 0.1])
aa = np.tile(a, (len(a), 1))
b = np.array([
    [0.3, 0.5, 0.2],
    [0.2, 0.2, 0.4],
    [0.3, 0.4, 0.2]
])
c = np.minimum(aa.T, b)
T = c.max(axis=0)
print("T=", T)
