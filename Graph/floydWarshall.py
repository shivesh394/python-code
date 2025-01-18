def floydWasrshall():
    for k in range(len(matrix)):         
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

matrix = [[0, 2, float('inf'), float('inf'), 8],
[2, 0, 3, float('inf'), 2],
[float('inf'), 3, 0, 1, float('inf')],
[float('inf'), float('inf'), 1, 0, 1],
[8, 2, float('inf'), 1, 0]]
floydWasrshall()
print(matrix)