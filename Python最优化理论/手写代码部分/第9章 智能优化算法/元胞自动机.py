import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
n = 200
fig, ax = plt.subplots()
Se = np.zeros((n, n))
z = np.zeros((n, n))
Se[int(n / 2 - 3):int(n / 2 + 2), int(n / 2 - 3):int(n / 2 + 2)] = 1
Sd = np.ones((n + 2, n + 2))
nums=100
def init():
    global Se
    img = plt.imshow(Se)
    return img
def update(step):
    global Se
    Sd[1:(n + 1), 1:(n + 1)] = Se
    sum = Sd[0:n, 1:n + 1] + Sd[2:n + 2, 1:n + 1] + Sd[1:n + 1, 0:n] + Sd[1:n + 1, 2:n + 2]  # 上下最优邻居之和
    Se = np.mod(sum, 2)
    img=plt.imshow(Se)
    return img
ani = FuncAnimation(fig, update, frames=nums,     #nums输入到frames后会使用range(nums)得到一系列step输入到update中去
                    init_func=init,interval=40)
plt.show()
