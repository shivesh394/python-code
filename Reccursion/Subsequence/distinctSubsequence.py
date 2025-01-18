def dfs(i, s, arr, l):
    if i >= len(arr):
        l.add(tuple(s.copy()))
        return 
    s.append(arr[i])
    dfs(i+1, s, arr, l)
    s.pop()
    dfs(i+1, s, arr, l)

l1 = set()
l2 = set()
a = 'abcdee'
a = 'eeabcd'


dfs(0, [], b, l1)
dfs(0, [], b, l2)
print(l1, len(l1))
print(l2, len(l2))



# power set and subsequence are not same in case of duplicate elemenet

