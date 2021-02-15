import gurobipy as grb

model = grb.Model()
x = model.addVar(name='x')
y = model.addVar(name='y')
model.setObjectiveN(x + 2 * y, index=0, weight=3, name='target1')
model.setObjectiveN(x - 3 * y, index=1, weight=0.5, name='target2')
