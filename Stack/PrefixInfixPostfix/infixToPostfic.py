def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
    
def infToPos(exp):
    stack = []
    ans = ''

    for s in exp:
        if s.isalnum():
            ans += s
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            if s == '^':
                while stack and prec(s) < prec(stack[-1]):
                    ans += stack.pop()
            else:
                while stack and prec(s) <= prec(stack[-1]):
                    ans += stack.pop()
            stack.append(s)
    while stack:
        ans += stack.pop()
    return ans


exp = 'a+b+c+d-e'
exp = '3^(1+1)'
exp = '((a-(b/c))*((d/k)-l))'
exp = 'a^b^c'
print(infToPos(exp))