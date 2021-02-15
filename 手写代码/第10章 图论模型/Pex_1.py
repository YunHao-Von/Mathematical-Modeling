import numpy as np
import networkx as nx
import pylab as plt

a = np.zeros((5, 5))
a[0, 1:5] = [9, 2, 4, 7]
a[1, 2:4] = [3, 4]
a[2, [3, 4]] = [8, 4]
a[3, 4] = 6
np.savetxt("Pdata10_2.txt",a)
i,j=np.nonzero(a)
w=a[i,j]
edges=list(zip(i,j,w))
G=nx.Graph()
G.add_weighted_edges_from(edges)
key=range(5)
s=[str(i+1) for i in range(5)]
s=dict(zip(key,s))
plt.rc("font",size=18)
plt.subplot(121)
nx.draw(G,font_weight='bold',labels=s)
plt.subplot(122)
pos=nx.shell_layout(G)
nx.draw_networkx(G,pos,node_size=260,labels=s)
w=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,font_size=12,edge_labels=w)
plt.show()