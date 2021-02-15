import numpy as np
from matplotlib.pyplot import *
x=np.linspace(0,2*np.pi,200)
y1=np.sin(x);y2=np.cos(x);y3=np.sin(x*x)
rc('font',size=16);rc('text',usetex=False)
ax1=subplot(2,2,1)
ax1.plot(x,y1,'r',label='$sin(x)$')
legend()
ax2=subplot(2,2,2)
ax2.plot(x,y2,'b--',label='$cos(x)$');legend()
ax3=subplot(2,1,2)
ax3.plot(x,y3,'k--',label='$sin(x^2)$')
legend()
savefig("figure2_39.png",dpi=500);show()