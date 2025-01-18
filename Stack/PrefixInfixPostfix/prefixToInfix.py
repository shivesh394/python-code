def prefixToInfix(infix):
    stack  = []
    for s in reversed(infix):
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            res = '(' + a + s + b + ')'
            stack.append(res)
    return stack[-1]

prefix = '*-a/bc-/dkl'
print(prefixToInfix(prefix))