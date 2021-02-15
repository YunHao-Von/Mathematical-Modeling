import numpy as np

r = np.array([
    [1, 1 / 5, -1 / 5],
    [1 / 5, 1, -2 / 5],
    [-1 / 5, -2 / 5, 1]
])
[val, vec] = np.linalg.eig(r)
A1 = np.tile(np.sqrt(val), (3, 1)) * vec
A2 = vec * np.sqrt(val)
num = int(input("请输入选择的公共因子的个数"))
A = A1[:, :num]
Ac=np.sum(A**2,axis=0)
print(Ac)