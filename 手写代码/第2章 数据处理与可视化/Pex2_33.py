import pandas as pd
a=pd.read_excel("Pdata2_33.xlsx",usecols=range(1,4))
b=a.values
c=a.describe()
print(c)
print(b)