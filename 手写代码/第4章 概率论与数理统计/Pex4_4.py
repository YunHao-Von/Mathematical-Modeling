from scipy.stats import binom
n,p=20,0.8
mean,variance,skewness,kurtosis=binom.stats(n,p,moments='mvsk')
print("所求的数字特征为：",binom.stats(n,p,moments='mvsk'))