a = [1,2,3,4,5,4,2,6,5,4,9]
k = 9
s = []
def dfs(i, sum):
    if i >= len(a):
        if sum == k:
            return 1
        return 0

    s.append(a[i])
    sum += a[i]
    l = dfs(i+1, sum)
    sum -= a[i]
    s.pop()
    r = dfs(i+1, sum)
    return l + r
    
print(dfs(0, 0))