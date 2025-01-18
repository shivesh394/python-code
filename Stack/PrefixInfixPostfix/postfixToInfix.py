def postfixToInfix(postfix):
    stack  = []
    for s in postfix:
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            res = '(' + b + s + a + ')'
            stack.append(res)
    return stack[-1]

# postfix = 'fr-AuwM+*+*'
postfix = '231*+9-'
print(postfixToInfix(postfix))