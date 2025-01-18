a = [4, 10, 5, 8, 20, 15, 3, 12]

ans = []
s = []


# for i in range(len(a)-1,-1,-1):
#     while s and s[-1] >= a[i]:
#         s.pop()
#     if not s:
#         ans.append(len(a))
#     elif s[-1] < a[i]:
#         ans.append(a.index(s[-1],i))
#     s.append(a[i])
# ans.reverse()


for i in range(len(a)-1,-1,-1):
    while s and a[s[-1]] >= a[i]:
        s.pop()
    if not s:
        ans.append(len(a))
    else:
        ans.append(s[-1])
    s.append(i)
ans.reverse()


print(ans) 