from scipy.stats import norm
from pylab import plot, fill_between, show, text, savefig, rc
from numpy import array, linspace, zeros

alpha = array([0.001, 0.005, 0.01, 0.025, 0.05, 0.10])
za = norm.ppf(1 - alpha, 0, 1)
print("上alpha分位数分别为：", za)
x = linspace(-4, 4, 100);
y = norm.pdf(x, 0, 1)
rc('font', size=16);
rc('text', usetex=False)
plot(x, y)
x2 = linspace(za[-1], 4, 100)
y2 = norm.pdf(x2)
y1 = [0] * len(x2)
fill_between(x2, y1, y2, color='r')
plot([-4,4],[0,0])
text(1.9,0.07,"$\\leftarrow\\alpha\$=0.1")
savefig("figure4_2.png",dpi=500)
show()