a = [2, 2, 1, 1, 1, 2]
a = [1, 2, 2]
a = [1, 2, 3, 1]

a.sort()
ans = set()

def permute(idx):
    if idx == len(a):
        ans.add(tuple(a.copy()))
        return
    
    for i in range(idx, len(a)):
        if i != idx and a[i] == a[idx]:
            continue
        a[idx], a[i] = a[i], a[idx]
        permute(idx + 1)
        a[idx], a[i] = a[i], a[idx]

permute(0)
print(ans, len(ans))