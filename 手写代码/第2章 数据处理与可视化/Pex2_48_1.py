from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
n,p=5,0.4
x=np.arange(6);y=binom.pmf(x,n,p)
plt.subplot(1,2,1);plt.plot(x,y,'ro')
plt.vlines(x,0,y,'k',lw=3,alpha=0.5)
plt.subplot(1,2,2);plt.stem(x,y,use_line_collection=True)
plt.show()