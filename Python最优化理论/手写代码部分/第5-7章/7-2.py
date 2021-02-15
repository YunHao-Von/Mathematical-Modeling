import gurobipy as grb

edge = {
    ('v1', 'a'): 0,
    ('a', 'b1'): 10,
    ('a', 'b2'): 20,
    ('b1', 'c1'): 30,
    ('b1', 'c2'): 10,
    ('b2', 'c1'): 5,
    ('b2', 'c2'): 20,
    ('c1', 'd'): 20,
    ('c2', 'd'): 10,
    ('d', 'v2'): 0
}
links, length = grb.multidict(edge)
m = grb.Model()
x = m.addVars(links, obj=length, name='flow')
for i in ['a', 'b1', 'b2', 'c1', 'c2', 'd']:
    if i == 'a':
        delta = 1
    elif i == 'd':
        delta = -1
    else:
        delta = 0
    name = 'C_%s' % i
    m.addConstr(
        sum(x[i, j] for i, j in links.select(i, '*')) - sum(x[j, i] for j, i in links.select('*', i)) == delta,
        name=name)
m.optimize()
for i,j in links:
    if (x[i,j].x>0):
        print('%-2s->%-2s: %d' % (i,j,edge[(i,j)]))