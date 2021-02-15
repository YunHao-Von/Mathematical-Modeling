import numpy as np

a = np.loadtxt("Pdata18_4.txt")
m, n = a.shape
amean = a.mean()
cmean = a.mean(axis=0)
r = cmean / amean
w = np.arange(1, m + 1)
yh = w.dot(a.sum(axis=1)) / w.sum()
yj = yh / n
yjh = yj * r
print("下一年度各季度的预测值:", yjh)
