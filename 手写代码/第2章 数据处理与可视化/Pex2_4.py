import numpy as np
a=np.random.randint(1,11,(3,5))
print(a)
print("维数",a.ndim)
print("维度",a.shape)
print("元素总数",a.size)
print("类型：",a.dtype)
print("每个元素的字节数",a.itemsize)