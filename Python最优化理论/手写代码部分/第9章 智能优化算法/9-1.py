import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
x=np.arange(-5,5,0.1)
y=np.arange(-5,5,0.1)
X,Y=np.meshgrid(x,y)
A=10
Z=2*A+X**2-A*np.cos(2*np.pi*X)+Y**2-A*np.cos(2*np.pi*Y)
fig=plt.figure()
ax=Axes3D(fig)
surf=ax.plot_surface(X,Y,Z,cmap=cm.coolwarm)
plt.show()