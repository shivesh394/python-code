n = int(input())
m = int(input())
l = []
for i in range(m):
    temp = list(map(int, input().split()))
    l.append(temp)
adj = [[] for i in range(n)]
for u, v in l:
    adj[v - 1].append(u - 1)


def dfs(i):
    vis[i] = 1
    for j in adj[i]:
        if j not in vis:
            dfs(j)
    stack.append(i + 1)

for i in range(n):
    vis = {}
    stack = []
    dfs(i)
    print(stack)