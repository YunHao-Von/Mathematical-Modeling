import numpy as np
a=[];b=[];c=[]
with open("Pdata2_21.txt") as file:
    for (i,line) in enumerate(file):
        elements=line.strip().split()
        if i <6:
            a.append(list(map(float,elements[:8])))
            b.append(float(elements[-1].rstrip('kg')))
        else:
            c=[float(x) for x in elements]
s=np.array(a)
b=np.array(b)
c=np.array(c)
print(a)
print(b)
print(c)