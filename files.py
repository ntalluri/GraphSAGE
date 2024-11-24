import numpy as np
import json 
from itertools import islice
import networkx as nx

a = np.load('example_data/toy-ppi-feats.npy')

print(a.shape)
print((a[1500]))

with open('example_data/toy-ppi-G.json', 'r') as file:
    ppi_graph = json.load(file)

# print(type(data))

# print(len(data))
print(ppi_graph.keys())

# third_item = next(islice(data.items(), 2, 3))
# print("Third item:", third_item)

G = nx.Graph()
for node in ppi_graph['nodes']:
    node_id = node.get('id')
    G.add_node(node_id, **node)

for link in ppi_graph['links']:
    source = link.get('source')
    target = link.get('target')
    G.add_edge(source, target)

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Is the graph connected?", nx.is_connected(G))
print("Number of connected components:", nx.number_connected_components(G))

print(G.nodes[1500])
print(type(G.nodes[1500]["feature"]))
