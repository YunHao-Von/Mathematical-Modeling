import gurobipy as grb
model = grb.Model()
t1 = [(1, 1), (1, 2), (1, 3),
      (2, 1), (2, 2), (2, 3),
      (3, 1), (3, 2), (3, 3)]
vars = model.addVars(t1, name='d')
c1=[(1,1),(1,2),(1,3)]
coeff=grb.tupledict(c1)
coeff[(1,1)]=1
coeff[(1,2)]=0.3
coeff[(1,3)]=0.4
print(vars.prod(coeff,1,'*'))