import numpy as np
from matplotlib.pyplot import plot, show, rc, legend, subplot
from scipy.optimize import curve_fit

rc('font', size=15)
rc('font', family='SimHei')
t0 = np.arange(1, 7)
x0 = np.array([
    5.081, 4.611, 5.1177, 9.3775, 11.0574, 11.0524
])
xt = np.polyfit(t0, x0, 1)
xh1 = np.polyval(xt, t0)
delta1 = abs((xh1 - x0)) / x0
x1 = np.cumsum(x0)
xh2 = lambda t, a, b, c: a * np.exp(b * t) + c
para, cov = curve_fit(xh2, t0, x1)
xh21 = xh2(t0, *para)
xh22 = np.r_[xh21[0], np.diff(xh21)]
delta2 = np.abs((xh22 - x0) / x0)
print("拟合的参数值为：", para)
subplot(121)
plot(t0, x0, 's')
plot(t0, xh1, '*-')
legend(('原始数据点', '线性拟合'), loc='upper left')
subplot(122)
plot(t0, x1, 'o')
plot(t0, xh21, 'p-')
legend(('累加数据点', '累加后拟合'))
show()
