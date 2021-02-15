import pandas as pd
import numpy as np
s=pd.Series([10.5,20.5,98],index=['a','b','c'])
print(s['b'])
b1=np.mean(s)
b2=s.mean()
print(b1)
print(b2)