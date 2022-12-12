from collections import deque

def dijkstra(graph, source, target):
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[source] = 0
    vtx = list(graph.keys())

    while vtx:
        cur = min(vtx, key=lambda v: dist[v])
        vtx.remove(cur)
        if dist[cur] == float('inf'):
            break
        for neigh in graph[cur]:
            cand = dist[cur] + 1
            if cand < dist[neigh]:
                dist[neigh] = cand
                prev[neigh] = cur

    path, cur = deque(), target
    while prev[cur] is not None:
        path.appendleft(cur)
        cur = prev[cur]
    if path:
        path.appendleft(cur)

    return dist[target]

def as_graph(matrix: list[str]):
    graph = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            vertex = (row, col)
            neighs = []
            # Connect the vertex to its neighbours. Note that the 'E' vertex has an implied value of 'z'.
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                    neigh = (r, c)
                    if matrix[r][c] == 'E':
                        w = ord('z')
                    else:
                        w = ord(matrix[r][c])
                    if matrix[row][col] == 'S' or w<=ord(matrix[row][col])+1:
                        neighs.append(neigh)
            # Add the vertex and its neighbours to the graph
            graph[vertex] = neighs

    return graph

def find_startpoints(matrix):
    return [
        (y, x)
        for y, row in enumerate(matrix)
        for x, elem in enumerate(row)
        if elem == 'a'
    ]

if __name__ == "__main__":
    with open("../d/12") as f:
        lines = f.readlines()

    # Convert the lines to a list of strings
    matrix = [list(line.strip()) for line in lines]
    g = as_graph(matrix)
    best = dijkstra(g, (20, 0), (20, 36))
    print(f'Part1: {best}')

    # Part 2: naive, slow, but correct, via brute-force and ignorance.
    for s in find_startpoints(matrix):
        b = dijkstra(g, s, (20, 36))
        if b<best:
            best = b
    print(f'Part2: {best}')

