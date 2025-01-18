def mul(x, y, n):
    if n == 0:
        return 0
    x_das = x[0 : n - 1]
    x1 = int(x[n - 1])
    m = mul(x_das, y, n - 1)
    return 10*m + x1*int(y)

x = '1234561234567812345672345678234567234567'
y = '1236989876543234567898765432345678987654'
print(mul(x, y, len(x)))