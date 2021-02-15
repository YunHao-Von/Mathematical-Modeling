import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

a = pd.read_excel("Pdata11_2.xlsx", header=None)
b = a.values
x0 = b[:-2, 1:-1].astype(float)
y0 = b[:-2, -1].astype(int)
x = b[-2:, 1:-1]
v = np.cov(x0.T)
knn = KNeighborsClassifier(3, metric='mahalanobis', metric_params={'V': v})
knn.fit(x0, y0)
print(knn.score(x0, y0))
