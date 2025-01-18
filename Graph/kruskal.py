class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n + 1)
        self.parent = []
        for i in range(n + 1):
            self.parent.append(i)

    def find_parent(self, node):
        if self.parent[node] == node:
            return node 
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ult_pu = self.find_parent(u)
        ult_pv = self.find_parent(v)
        if ult_pu == ult_pv:
            return
        if self.rank[ult_pu] > self.rank[ult_pv]:
            self.parent[ult_pv] = ult_pu
        elif self.rank[ult_pv] > self.rank[ult_pu]:
            self.parent[ult_pu] = ult_pv
        else:
            self.parent[ult_pv] = ult_pu
            self.rank[ult_pu] += 1

# edges = []
# for u in range(V):
#     for v, wt in adj[u]:
#         edges.append([wt, u, v])

V = 3
edges = [[5, 0, 1], [1, 0, 2], [5, 1, 0], [3, 1, 2], [3, 2, 1], [1, 2, 0]]

V = 4
edges = [[6, 1, 2], [2, 2, 3], [2, 1, 3], [2, 1, 0]]
edges.sort()
ds = DisjointSet(V)
ans = 0
for wt, u, v in edges:
    if ds.find_parent(u) != ds.find_parent(v):
        ans += wt
        ds.unionByRank(u, v)
print(ans)