import gurobipy as grb

# 两种商品
commodities = ['Pencils', 'Pens']
# 2个产地+3个目的地
nodes = ['Detroit', 'Denver', 'Boston', 'New York', 'Seattle']
arcs, capacity = grb.multidict({
    ('Detroit', 'Boston'): 100,
    ('Detroit', 'New York'): 80,
    ('Detroit', 'Seattle'): 120,
    ('Denver', "Boston"): 120,
    ('Denver', 'New York'): 120,
    ('Denver', 'Seattle'): 120
})
cost = {
    ('Pencils', 'Detroit', 'Boston'): 10,
    ('Pencils', 'Detroit', 'New York'): 20,
    ('Pencils', 'Detroit', 'Seattle'): 60,
    ('Pencils', 'Denver', 'Boston'): 40,
    ('Pencils', 'Denver', 'New York'): 40,
    ('Pencils', 'Denver', 'Seattle'): 30,
    ('Pens', 'Detroit', 'Boston'): 20,
    ('Pens', 'Detroit', 'New York'): 20,
    ('Pens', 'Detroit', 'Seattle'): 80,
    ('Pens', 'Denver', 'Boston'): 60,
    ('Pens', 'Denver', 'New York'): 70,
    ('Pens', 'Denver', 'Seattle'): 30,
}
inflow = {
    ('Pencils', 'Detroit'): 50,
    ('Pencils', 'Denver'): 60,
    ('Pencils', 'Boston'): -50,
    ('Pencils', 'New York'): -50,
    ('Pencils', 'Seattle'): -10,
    ('Pens', 'Detroit'): 60,
    ('Pens', 'Denver'): 40,
    ('Pens', 'Boston'): -40,
    ('Pens', 'New York'): -30,
    ('Pens', 'Seattle'): -30
}
m = grb.Model('netflow')
flow = m.addVars(commodities, arcs, obj=cost, name='flow')
print(type(flow))
print(len(flow))
print(flow)
# m.addConstrs((flow.sum('*', i, j) <= capacity[i, j] for i, j in arcs), 'cap')
# m.addConstrs((flow.sum(h, '*', j) + inflow[h, j] == flow.sum(h, j, '*') for h in commodities for j in nodes), "node")
# m.optimize()
# if m.status == grb.GRB.Status.OPTIMAL:
#     solution=m.getAttr('x',flow)
#     for h in commodities:
#         print('\nOptimal flows for %s:' % h)
#         for i,j in arcs:
#             if solution[h,j,i]>0:
#                 print('%s -> %s: %g' % (i,j,solution[h,i,j]))