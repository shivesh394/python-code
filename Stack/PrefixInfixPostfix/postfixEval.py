def solve(a, b, s):
    # res = 0
    if s == '+':
        res = int(a) + int(b)
    elif s == '-':
        res = int(a) - int(b)
    elif s == '*':
        res = int(a) * int(b)
    elif s == '/':
        res = int(a) / int(b)
    elif s == '^':
        res = int(a) **  int(b)
    return res

op = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
        }



def postfixEval(postfix):
    stack = []
    for s in postfix:
        if s.isnumeric():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(solve(b, a, s))
    return stack[-1]


# postfix = '231*+9-'
postfix = '234^^'
postfix = '53+62/*35*+'
postfix = '234*+223^/-'
# postfix = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(postfixEval(postfix))