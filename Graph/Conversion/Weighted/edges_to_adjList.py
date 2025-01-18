V = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
adj = [[] for _ in range(V)]
print(adj)
for u, v, wt in edges:
    adj[u].append([v, wt])
    adj[v].append([u, wt])
print(adj)