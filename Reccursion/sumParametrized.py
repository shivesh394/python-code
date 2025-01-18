def fun(n, sum):
    if n == 0:
        print(sum)
        return
    else:
        fun(n - 1, n + sum)

fun(10,0)