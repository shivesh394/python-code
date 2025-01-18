a = [4, 10, 5, 8, 20, 15, 3, 12] # incresing stack

ans = []
s = []
for i in range(len(a)-1,-1,-1):
    while s and s[-1] >= a[i]:
        s.pop()
    ans.append(s[-1]) if s else ans.append(-1)
    s.append(a[i])
ans.reverse()
print(ans) 