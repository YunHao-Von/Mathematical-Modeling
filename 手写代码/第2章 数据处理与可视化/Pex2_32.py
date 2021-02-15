import pandas as pd
a=pd.read_csv("Pdata2_32.txt",sep=",",parse_dates={'birthday':[0,1,2]},skiprows=2,
              skipfooter=2,comment='#',thousands='&',engine="python")
print(a)