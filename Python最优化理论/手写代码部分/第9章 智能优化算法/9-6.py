import numpy as np
import matplotlib.pyplot as plt


# 有放回的抽样
# a = np.random.choice([1, 2, 3, 4, 5, 6], size=6, p=[0.19, 0.22, 0.18, 0.09, 0.13, 0.19])
# print(a)
def fitness_func(X):
    '''此函数用于计算适应度值'''
    a = 10
    pi = np.pi
    x = X[:, 0]
    y = X[:, 1]
    return 2 * a + x ** 2 - a * np.cos(2 * pi * x) + y ** 2 - a * np.cos(2 * pi * y)


def decode(x, a, b):
    '''解码。把基因型解码成为表现型'''
    xt = 0
    for i in range(len(x)):
        xt = xt + x[i] * np.power(2, i)
    return a + xt * (b - a) / (np.power(2, len(x)) - 1)


def decode_X(X: np.array):
    X2 = np.zeros((X.shape[0], 2))
    for i in range(X.shape[0]):
        xi = decode(X[i, :20], -5, 5)
        yi = decode(X[i, 20:], -5, 5)
        X2[i, :] = np.array([xi, yi])
    return X2


def select(X, fitness):
    '''根据轮盘赌法来选择优秀个体'''
    fitness = 1 / fitness
    fitness = fitness / fitness.sum()
    idx = np.array(list(range(X.shape[0])))
    X2_idx = np.random.choice(idx, size=X.shape[0], p=fitness)
    X2 = X[X2_idx, :]
    return X2


def crossover(X, c):
    '''按顺序选择2个个体与概率c来进行交叉操作'''
    for i in range(0, X.shape[0], 2):
        xa = X[i, :]
        xb = X[i + 1, :]
        for j in range(X.shape[1]):
            if np.random.rand() <= c:
                xa[j], xb[j] = xb[j], xa[j]
        X[i, :] = xa
        X[i + 1, :] = xb
    return X


def mutation(X, m):
    '''变异操作'''
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if np.random.rand() <= m:
                X[i, j] = (X[i, j] + 1) % 2
    return X


def ga():
    '''遗传算法的主函数'''
    c = 0.3  # 交叉概率
    m = 0.05  # 变异概率
    best_fitness = []  # 记录每次迭代的结果
    best_xy = []
    iter_num = 100  # 最大迭代次数
    X0 = np.random.randint(0, 2, (50, 40))  # 随机初始化种群，是50*40的0-1矩阵
    for i in range(iter_num):
        X1 = decode_X(X0)  # 染色体解码
        fitness = fitness_func(X1)  # 计算个体适应度
        X2 = select(X0, fitness)  # 选择操作
        X3 = crossover(X2, c)  # 交叉操作
        X4 = mutation(X3, m)  # 变异操作
        X5 = decode_X(X4)
        fitness = fitness_func(X5)
        best_fitness.append(fitness.min())
        x,y=X5[fitness.argmin()]
        best_xy.append((x, y))
        X0 = X4
    print("最优值是：", best_fitness[-1])
    print("最优解是：", best_xy[-1])
    plt.plot(best_fitness, color='r')
    plt.show()
ga()
