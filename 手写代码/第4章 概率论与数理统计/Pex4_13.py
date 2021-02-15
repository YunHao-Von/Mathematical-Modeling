import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
a=np.loadtxt("Pdata4_6_2.txt")
h=a[:,::2]
h=h.flatten()
mu=np.mean(h)
s=np.std(h)
print("样本均值和方差为：",[mu,s])
print(norm.fit(h))