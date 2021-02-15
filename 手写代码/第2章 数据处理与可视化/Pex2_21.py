import numpy as np
a=np.genfromtxt("Pdata2_21.txt",max_rows=6,usecols=range(8))
b=np.genfromtxt("Pdata2_21.txt",dtype=str,max_rows=6,usecols=[8])
b=[float(v.rstrip('kg'))  for (i,v) in enumerate(b)]
c=np.genfromtxt("Pdata2_21.txt",skip_header=6)
print(a,'\n',b,'\n',c)