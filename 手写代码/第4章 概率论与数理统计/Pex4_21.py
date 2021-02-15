import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
a=np.loadtxt("Pdata4_6_2.txt")
w=a[:,1::2]
w=w.flatten()
mu=w.mean()
s=w.std(ddof=1)
print(mu,s)
statVal,pVal=ss.kstest(w,'norm',(mu,s))
print(statVal,pVal)