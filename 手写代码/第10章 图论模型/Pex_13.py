import numpy as np
import networkx as nx
import pylab as plt

L = [(1, 2, 8),(1,3,4),(2,3,4),(3,4,2),(1,5,2),(3,5,1),(4,5,5) ]
b=nx.Graph()
b.add_nodes_from(range(1,6))
b.add_weighted_edges_from(L)
T=nx.minimum_spanning_tree(b,weight='weight',algorithm='prim')
w=nx.get_edge_attributes(T,'weight')
TL=sum(w.values())
print("最小生成树为：",w)
print("最小生成树的长度为：",TL)
pos=nx.shell_layout(b)
nx.draw(T,pos,node_size=280,with_labels=True,node_color='r')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w)
plt.show()