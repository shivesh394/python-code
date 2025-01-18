class DisjointSet:
    def __init__(self, V):
        self.rank = [0]*(V + 1)
        self.parent = [i for i in range(V + 1)] 
    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    def union(self, u, v):
        ult_pu = self.find_parent(u)
        ult_pv = self.find_parent(v)
        if self.rank[ult_pu] > self.rank[ult_pv]:
            self.parent[ult_pv] = ult_pu
        else:
            self.parent[ult_pu] = ult_pv
            if self.rank[ult_pu] == self.rank[ult_pv]:
                self.rank[ult_pv] += 1


ds = DisjointSet(7)
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
if ds.find_parent(3) == ds.find_parent(7):
    print('Connected')
else:
    print('Not connected')
ds.union(3, 7)
if ds.find_parent(3) == ds.find_parent(7):
    print('Connected')
else:
    print('Not connected')
