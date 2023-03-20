import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([
    ('RMUTT', 'NBU', {'distance': 9.5}),
    ('RMUTT', 'EAU', {'distance': 4.5}),
    ('RMUTT', 'VRU', {'distance': 35.9}),
    ('RMUTT', 'TU', {'distance': 16.8}),
    ('EAU', 'TU', {'distance': 20.3}),
    ('EAU', 'BU', {'distance': 19.7}),
    ('EAU', 'NBU', {'distance': 9.2}),
    ('BU', 'TU', {'distance': 3.7}),
    ('BU', 'NBU', {'distance': 17.5}),
    ('BU', 'PTU', {'distance': 16.2}),
    ('BU', 'RPU', {'distance': 41.2}),
    ('BU', 'RSU', {'distance': 18}),
    ('TU', 'VRU', {'distance': 13.8}),
    ('TU', 'PTU', {'distance': 15}),
    ('TU', 'MRU', {'distance': 34.8}),
    ('VRU', 'MRU', {'distance': 35.9}),
    ('PTU', 'MRU', {'distance': 22}),
    ('PTU', 'RPU', {'distance': 27.4}),
    ('MRU', 'RPU', {'distance': 20.7}),
    ('RPU', 'RSU', {'distance': 34.7}),
    ('RSU', 'NBU', {'distance': 13.7}),
    ('KMUTNB', 'RSU', {'distance': 30.3}),
    ('KMUTNB', 'RPU', {'distance': 43.5}),
    ('KMUTNB', 'MU', {'distance': 24.6}),
    ('KMUTNB', 'CU', {'distance': 17.5}),
    ('KMUTNB', 'NBU', {'distance': 18.1}),
    ('MU', 'CU', {'distance': 29.2}),
    ('MU', 'KMUTT', {'distance': 33.8}),
    ('CU', 'KMUTT', {'distance': 15.1}),
    ('CU', 'KMITL', {'distance': 33.3}),
    ('KMITL', 'KMUTT', {'distance': 46.6}),
    ('KMITL', 'NBU', {'distance': 39.2}),
])

def search_nodes():
    global shortest_path
    print("['BU', 'RMUTT', 'TU', 'NBU', 'PTU', 'MRU', 'RSU', 'RPU', 'VRU', 'EAU', 'MU', 'KMUTNB', 'CU', 'KMUTT', 'KMITL']")
    source = input("Enter beginning from: ")
    dest = input("Enter destination: ")
    shortest_path = nx.shortest_path(G, source=source, target=dest, weight='distance')
    print(f"Shortest path from {source} to {dest}: {shortest_path}")
    shortest_path_length = nx.shortest_path_length(G, source=source, target=dest, weight='distance')
    shortest_path_length = ("%.2f"%(shortest_path_length))
    print(f"Shortest path length: {shortest_path_length}"" km")

search_nodes()

pos = nx.spring_layout(G, seed=42)
node_color_map = []
for node in G.nodes():
    if node == shortest_path[0]:
        node_color_map.append('green')
    elif node == shortest_path[-1]:
        node_color_map.append('red')
    elif node in shortest_path:
        node_color_map.append('orange')
    else:
        node_color_map.append('gray')
        
nx.draw(G, pos, with_labels=True, node_color=node_color_map, node_size=1000)

edge_labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Draw the route
edge_list = list(zip(shortest_path, shortest_path[1:]))

plt.title("Distance of University", size=12)
plt.show()