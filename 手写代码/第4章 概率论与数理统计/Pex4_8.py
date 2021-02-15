import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt("Pdata4_6_2.txt")
h = a[:, ::2]
w = a[:, 1::2]
h = np.reshape(h, (-1, 1))
w = np.reshape(w, (-1, 1))
plt.rc("font", size=16)
plt.rc("font", family="SimHei")
plt.subplot(121)
plt.xlabel("身高")
plt.hist(h, 10)
plt.subplot(122)
ps = plt.hist(w, 6)
plt.xlabel("体重")
print("体重的频数表为：", ps)
plt.show()
