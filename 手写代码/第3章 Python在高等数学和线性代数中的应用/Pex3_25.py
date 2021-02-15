from scipy.optimize import minimize
f=lambda x: 100*(x[1]-x[0]**2)**2+(1-x[0])**2
x0=minimize(f,[2.0,2.0])
print(x0.x)
print(x0.fun)