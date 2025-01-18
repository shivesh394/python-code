def fib(n):
    if n <= 1:
        return n 
    return fib(n - 1) + fib(n - 2)

print(fib(10))

# TC - O(2^n)
# SC - O(1)