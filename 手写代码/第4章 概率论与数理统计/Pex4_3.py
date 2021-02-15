from scipy.stats import binom
n,p=20,0.8
print("期望和方差的分布为：",binom.stats(n,p))