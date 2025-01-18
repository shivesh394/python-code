n = 4
col = set()
pD = set()
nD = set()
import copy
ans = []
# b = [["."]*n]*n  # this wrong because all list inside list refrence to same address
b = [['.']*n for i in range(n)]

def dfs(r):
    if r == n:
        # copy = ["".join(row) for row in b]
        # ans.append(copy)
        ans.append(copy.deepcopy(b))
        return
    for c in range(n):
        if c in col or (r+c) in pD or (r-c) in nD:
            continue
        col.add(c)
        pD.add(r+c)
        nD.add(r-c)
        b[r][c] = "Q"
        dfs(r + 1)
        col.remove(c)
        pD.remove(r+c)
        nD.remove(r-c)
        b[r][c] = "."
dfs(0)
print(ans)