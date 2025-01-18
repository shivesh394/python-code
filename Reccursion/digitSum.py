def sum(n):
    while n > 9:
        sum = 0
        while n:
            sum += n % 10
            n //= 10
        n = sum
    return n
print(sum(10009998))