a = [1,2,3,1]
a = [1, 2, 2]
a = [2, 2, 1, 1, 1, 2]

a.sort()
ans = []

def permute(a, idx):
    if idx == len(a):
        ans.append(a.copy())
        return
    for i in range(idx,len(a)):
        if i != idx and a[i] == a[idx]:
            continue
        a[idx], a[i] = a[i], a[idx]
        permute(a.copy(), idx + 1)


permute(a.copy(), 0)
print(ans, len(ans))