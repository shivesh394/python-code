def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def dfs(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 'Q'
            dfs(board, col + 1, n, solutions)
            board[i][col] = '.'

n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
print(board)
solutions = []
dfs(board, 0, n, solutions)

# Now 'solutions' contains all the solutions.
for solution in solutions:
    for row in solution:
        print(' '.join(row))
    print("\n")



