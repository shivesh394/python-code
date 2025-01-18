V = 8
edges = [[1, 2], [3, 5], [6, 3], [6, 5], [7, 3], [7, 1]]
adjList = [[] for _ in range(V)]
for u, v in edges:
    adjList[u].append(v)
print(adjList)