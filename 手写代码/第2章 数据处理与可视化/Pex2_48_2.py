from scipy.stats import binom
import pylab as plt
n,p=5,0.4
x=plt.arange(6);y=binom.pmf(x,n,p)
plt.subplot(121);plt.plot(x,y,'ro')
plt.vlines(x,0,y,'k',lw=3,alpha=0.5)
plt.subplot(122);plt.stem(x,y,use_line_collection=True)
plt.show()