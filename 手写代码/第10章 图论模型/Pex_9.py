import numpy as np
import networkx as nx
import pylab as plt

p = [25, 26, 28, 31]
a = [10, 14, 18, 26]
r = [20, 16, 13, 11]
b = np.zeros((5, 5))
for i in range(5):
    for j in range(i + 1, 5):
        b[i, j] = p[i] + np.sum(a[0:j - i]) - r[j - i - 1]
print(b)
G = nx.DiGraph(b)
p = nx.dijkstra_path(G, source=0, target=4, weight='weight')
print("最短路径为：", np.array(p) + 1)  # 注意这里的+1
d = nx.dijkstra_path_length(G, 0, 4, weight="weight")
print("所求的最小费用是：", d)
s = dict(zip(range(5), range(1, 6)))
plt.rc('font',size=16)
pos=nx.shell_layout(G)
w=nx.get_edge_attributes(G,'weight')
nx.draw(G,pos,font_weight='bold',label=s,node_color='green')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
path_edges=list(zip(p,p[1:]))
nx.draw(G,pos,edgelist=path_edges,edge_color='r',width=3)
plt.show()