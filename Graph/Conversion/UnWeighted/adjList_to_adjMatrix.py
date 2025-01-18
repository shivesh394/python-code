V = 8
adj = [[], [2], [], [5], [], [], [3, 5], [3, 1]]
adjMatrix = [[float('inf')]*V for _ in range(V)]
for u in range(V):
    for v in adj[u]:
        adjMatrix[u][v] = 1
print(adjMatrix)
