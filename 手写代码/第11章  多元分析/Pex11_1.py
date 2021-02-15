import numpy as np
from sklearn.neighbors import KNeighborsClassifier

x0 = np.array([
    [1.24, 1.27], [1.36, 1.74], [1.38, 1.64], [1.38, 1.82], [1.38, 1.90], [1.40, 1.70], [1.48, 1.82], [1.54, 1.82],
    [1.56, 2.08], [1.14, 1.78], [1.18, 1.96], [1.20, 1.86], [1.26, 2.00], [1.28, 2.00], [1.30, 1.96]
])
x = np.array([
    [1.24, 1.80], [1.28, 1.84], [1.4, 2.04]
])
g = np.hstack([np.ones(9), 2 * np.ones(6)])
v = np.cov(x0.T)
knn = KNeighborsClassifier(2, metric='mahalanobis', metric_params={'V': v})
knn.fit(x0, g)
pre = knn.predict(x)
print("马氏距离的分类结果是：", pre)
print(knn.score(x0,g))
