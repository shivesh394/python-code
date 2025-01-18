n = 4
ans = []
# b = [['.']*n]*n
# b = [['.']*n for i in range(n)]
b = [['.' for _ in range(n)] for _ in range(n)]

def isSafe(row, col):
    
    dRow = row
    dCol = col

    while row >= 0 and col >= 0:
        if b[row][col] == 'Q':
            return 0
        row -= 1
        col -= 1

    row = dRow
    col = dCol

    while col >= 0:
        if b[row][col] == 'Q':
            return 0
        col -= 1

    row = dRow
    col = dCol

    while row < n and col >= 0:
        if b[row][col] == 'Q':
            return 0
        row += 1
        col -= 1
    return 1


def dfs(col):
    if col == n:
        print(b)
        x = b.copy()
        ans.append(x)
        # copy = ["".join(row) for row in b]
        # ans.append(copy)
        print(ans)
        return
    
    for row in range(n):
        if isSafe(row, col):
            b[row][col] = 'Q'
            dfs(col+1)
            b[row][col] = '.'
        
dfs(0)
print(ans)