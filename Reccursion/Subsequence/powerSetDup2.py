def dfs(i, s, arr, l):
    if i >= len(arr):
        l.add(tuple(s.copy()))
        return 
    s.append(arr[i])
    dfs(i+1, s, arr, l)
    s.pop()
    dfs(i+1, s, arr, l)

res = set()
b = '1231'
b =sorted(b)
dfs(0, [], b, res)
print(res, len(res))


# power set and subsequence are not same in case of duplicate elemenet