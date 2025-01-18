a = [1,2,3,4,5,4,2,6,5,4,9]
k = 9
l = set()
s = []
c = 0
def dfs(i, sum):
    if i >= len(a):
        if sum == k:
            l.add(tuple((s.copy())))
        return
    sum += a[i]
    s.append(a[i])
    dfs(i+1, sum)
    sum -= a[i]
    s.pop()
    dfs(i+1, sum)
dfs(0, 0)

print(list(l))