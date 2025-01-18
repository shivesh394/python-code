def subset_sum(a: list, n: int, sum: int):
    for i in range(1, n+1):
        for j in range(sum + 1):
            if a[i-1] <= j:
                tab[i][j] = tab[i-1][j] + tab[i-1][j-a[i-1]]
            else:
                tab[i][j] = tab[i-1][j]
    return tab[n][sum]


# a = [0, 0, 1]
# sum = 1
# a = [1, 1, 1, 1]
# sum = 4
# a = [1, 0, 8, 5, 1, 4]
# sum = 2
a = [1, 4, 4, 5]
sum = 5

n = len(a)
tab = [[0] * (sum + 1) for i in range(n + 1)]
tab[0][0] = 1
print(subset_sum(a, n, sum))
print(tab)