import pandas as pd
import numpy as np
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))
b=a.values
c=pd.DataFrame(b,index=np.arange(1,11),columns=["用户A","用户B","用户C"])
f=pd.ExcelWriter('Pdata2_34.xlsx')
c.to_excel(f,"sheet1")
c.to_excel(f,"sheet2")
f.save()