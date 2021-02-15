import numpy as np
from statsmodels.stats.weightstats import ztest
a=np.array([
    3.25,3.27,3.24,3.26,3.24
])
tstat,pvalue=ztest(a,value=21,alternative='smaller')
print(tstat,pvalue)