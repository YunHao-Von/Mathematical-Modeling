import pandas as pd
import numpy as np
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))
b1=a.iloc[np.arange(6),[0,1]]
b2=a.loc[np.arange(6),["用户A","用户B"]]