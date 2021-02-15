from sklearn.linear_model import Perceptron
import numpy as np

x0 = np.array([
    [-0.5, -0.5, 0.3, 0.3],
    [-0.5, 0.5, -0.5, 1.0]
]).T
y0 = np.array([1, 1, 0, 0])
md = Perceptron(tol=1e-3)
md.fit(x0, y0)
print(md.coef_, md.intercept_)
print(md.score(x0, y0))
print("预测值为:\n", md.predict(np.array([[-0.5, 0.2]])))
