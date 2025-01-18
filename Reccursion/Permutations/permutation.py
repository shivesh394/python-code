a = [1,2,3]
ans = []

def permute(idx):
    if idx >= len(a):
        ans.append(a.copy())
        return
    for i in range(idx,len(a)):
        a[idx], a[i] = a[i], a[idx]
        permute(idx + 1)
        a[idx], a[i] = a[i], a[idx]

permute(0)
print(ans)
print(len(ans))
