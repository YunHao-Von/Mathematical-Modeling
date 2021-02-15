from scipy.optimize import linprog
c=[-90,-64]
A=[
    [1,1],
    [12,8]
]
b=[
    [50],
    [480]
]
bound=((0,100/3.0),(0,None))
res=linprog(c,A,b,None,None,bound,method='simplex',options={"disp":True})
print(res)