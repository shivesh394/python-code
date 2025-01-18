a = [4, 10, 5, 8, 20, 15, 3, 12]

ans = []
s = []
for i in range(len(a)):
    while s and s[-1] >= a[i]:
        s.pop()
    if not s:
        ans.append(-1)
    elif s[-1] < a[i]:
        ans.append(s[-1])
    s.append(a[i])
print(ans) 