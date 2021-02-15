from ortools.graph import pywrapgraph

start_nodes = [1, 1, 1, 2, 4, 4, 3, 3, 5]
end_nodes = [2, 4, 3, 6, 6, 5, 4, 5, 6]
capacities = [70, 90, 100, 80, 100, 40, 40, 70, 90]
max_flow=pywrapgraph.SimpleMaxFlow()
for i in range(len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i],end_nodes[i],capacities[i])
if max_flow.Solve(1,6)==max_flow.OPTIMAL:
    print('最大流是：',max_flow.OptimalFlow())