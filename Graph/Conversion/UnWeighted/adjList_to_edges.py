V = 8
adj = [[], [2], [], [5], [], [], [3, 5], [3, 1]]
edges = []
for u in range(V):
    for v in adj[u]:
        edges.append([u, v])
print(edges)