import numpy as np,pandas as pd
from matplotlib.pyplot import *
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))
c=np.sum(a)
ind=np.array([1,2,3]);width=0.2
rc("font",size=16);bar(ind,c,width);ylabel("消费数据")
xticks(ind,['用户A','用户B','用户C'],rotation=20)
rcParams['font.sans-serif']=['SimHei']
savefig('font2_36.png',dpi=500)
show()