import gurobipy as grb

model = grb.Model()
t1 = [(1, 1), (1, 2), (1, 3),
      (2, 1), (2, 2), (2, 3),
      (3, 1), (3, 2), (3, 3)]
vars = model.addVars(t1, name='d')
print(sum(vars.select(1,'*')))
