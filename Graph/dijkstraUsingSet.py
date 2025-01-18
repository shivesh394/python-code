V = 2
adj= [[[1, 9]], [[0, 9]]]
S = 0
from sortedcontainers import SortedSet
dist = [float('inf')]*V
dist[S] = 0
s = SortedSet()
s.add((0, S))
while s:
    dis, node = s.pop(0)
    # dis, node = s[0]
    # s.remove((dis,node))
    for adjNode, adjDis in adj[node]:
        if dis + adjDis < dist[adjNode]:
            if dist[adjNode] != float('inf'):
                s.remove((dist[adjNode],adjNode))
            dist[adjNode] = dis + adjDis
            s.add((dis + adjDis, adjNode))
print(dist)