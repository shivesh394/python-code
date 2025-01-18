def solve(a, b, s):
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



def postfixEval(postfix):
    stack = []
    for s in reversed(postfix):
        if s.isnumeric():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(solve(a, b, s))
    return stack[-1]


postfix = '-+2*34/2^23'

print(postfixEval(postfix))