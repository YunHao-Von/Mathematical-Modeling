import gurobipy as grb

flow = {
    (0, 1): 99999,
    (1, 2): 70, (1, 3): 100, (1, 4): 90,
    (2, 6): 80,
    (3, 4): 40, (3, 5): 70,
    (4, 5): 40, (4, 6): 100,
    (5, 6): 90,
    (6, 7): 99999
}
arch,maxflow=grb.multidict(flow)
m=grb.Model('maxflow')
X=m.addVars(arch,name='X')
for i,j in arch:
    m.addConstr(X[i,j]<=maxflow[i,j])
    if i==0 or j==7:
        continue
    else:
        m.addConstr(X.sum(i,'*') == X.sum('*',i))#使其满足等式约束
m.setObjective(X.sum(1,'*'),sense=grb.GRB.MAXIMIZE)
m.optimize()
print("目标函数值 :",m.objVal)
for i,j in arch:
    print("%d->%d: %d" % (i,j,X[i,j].x))