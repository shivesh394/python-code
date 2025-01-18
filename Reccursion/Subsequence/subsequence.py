def dfs(i, s, arr, l):
    if i >= len(arr):
        l.append(s.copy())
        return 
    s.append(arr[i])
    dfs(i+1, s, arr, l)
    s.pop()
    dfs(i+1, s, arr, l)

l1 = []
l2 = []
a ='ljmolmti'
b = 'dfgh'
dfs(0, [], a, l1)
dfs(0, [], b, l2)

print(l1, len(l1))
print(l2)