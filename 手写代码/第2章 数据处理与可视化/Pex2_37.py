import numpy as np
from matplotlib.pyplot import *
x=np.array(range(8))
y='27.0 26.8 26.5 26.3 26.1 25.7 25.3 24.8'
y=",".join(y.split())
y=np.array(eval(y))
scatter(x,y)
savefig('figure2_23.png',dpi=500)
show()