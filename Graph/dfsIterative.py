graph = [[0,1,0,1,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,1,1,0,0],
        [1,0,1,0,1,0,0],
        [0,0,1,1,0,1,1],
        [0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0]]

vis = [0,0,0,0,0,0,0]

def dfs(i):
    stack = []
    stack.append(i)
    vis[i] = 1
    while stack:
        u = stack.pop()
        print(u, end = " ")
        for v in range(7):
            if graph[u][v] == 1 and not vis[v]:
                stack.append(v)
                vis[v] = 1

dfs(0)