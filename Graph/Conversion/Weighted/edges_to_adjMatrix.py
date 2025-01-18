V = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
adjMatrix = [[float('inf')]*V for i in range(V)]
for u, v, wt in edges:
    adjMatrix[u][v] = wt
    adjMatrix[v][u] = wt

for u in range(V):
    print(adjMatrix[u])
