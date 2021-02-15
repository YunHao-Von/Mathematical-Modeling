import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set_style('whitegrid')
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
np.random.seed(1234)
city_num = 10
iter_num = 1000
X = np.random.choice(list(range(1, 100)), size=city_num, replace=False)
Y = np.random.choice(list(range(1, 100)), size=city_num, replace=False)
plt.scatter(X, Y, color='r')
plt.title('城市分布坐标图')
plt.show()
