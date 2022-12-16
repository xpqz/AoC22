import itertools
import re
import networkx as nx

patt = r'Valve ([A-Z]{2})[^\d]+(\d+)[; a-z]+(.+)'

with open('/Users/stefan/work/AoC22/d/16') as f:
    data = f.read().splitlines()

spec = [re.findall(patt, row)[0] for row in data]

G = nx.Graph()
dist = {}
for node, flow, _ in spec:
    G.add_node(node, flow=int(flow))
    dist[node] = {}

for node, _, conn in spec:
    for neigh in conn.split(', '):
        G.add_edge(node, neigh)

# Find shortest path between all nodes
for a, b in itertools.product(dist.keys(), repeat=2):
    if a != b and G.nodes[b]['flow'] != 0:
        dist[a][b] = len(nx.shortest_path(G, a, b)) - 1

def part1():
    best = 0
    def search(opened, flow, cur, rem):
        nonlocal best
        best = max(best, flow)
        if rem <= 0:
            return

        if cur not in opened:
            search(opened.union([cur]), flow + G.nodes[cur]['flow'] * rem, cur, rem - 1)
        else:
            for k in set(dist[cur].keys())-opened:
                search(opened, flow, k, rem - dist[cur][k])

    search(set(['AA']), 0, 'AA', 29)
    return best

def part2():
    best = 0
    def search(opened, flow, cur, rem, elephant):
        nonlocal best
        best = max(best, flow)

        if rem <= 0:
            return

        if cur not in opened:
            search(opened.union([cur]), flow + G.nodes[cur]['flow'] * rem, cur, rem - 1, elephant)
            if not elephant:
                search(set([cur]).union(opened), flow + G.nodes[cur]['flow'] * rem, 'AA', 25, True)
        else:
            for k in set(dist[cur].keys())-opened:
                search(opened, flow, k, rem - dist[cur][k], elephant)

    search(set(['AA']), 0, 'AA', 25, False)
    return best

print(part1())
print(part2())