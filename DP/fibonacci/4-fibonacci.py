def fib(n):
    first = 0
    second = 1
    for i in range(2, n + 1):
        third = first + second
        first = second
        second = third
    return third

n = 10
print(fib(n))


# TC - O(n)
# SC - O(1)