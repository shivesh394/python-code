op = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: int(a / b),
    "*": lambda a, b: a * b
}


ans = op['*'](100,205)
print(ans)