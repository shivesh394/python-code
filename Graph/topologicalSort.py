vis = {}
stack = []
def dfs(i):
    vis[i] = 1
    for j in adj[i]:
        if j not in vis:
            dfs(j)
    stack.append(i)


V = 8
adj = [[], [2], [], [5], [], [], [3, 5], [3, 1]]
V = 5
adj = [[2, 3], [0], [1], [4], []]

for i in range(V):
    if i not in vis:
        dfs(i)
stack.reverse()
print(stack)