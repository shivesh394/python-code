a = [42, 46, 43, 28, 37, 42, 5, 3, 4]
k = 3
s = []
def dfs(i, sum):
    if i >= len(a):
        if sum == k:
            print(s.copy())
            return True
        return False

    s.append(a[i])
    sum += a[i]
    if dfs(i+1, sum):
        return True
    sum -= a[i]
    s.pop()
    if(dfs(i+1, sum)):
        return True
    return False
    
print(dfs(0, 0))