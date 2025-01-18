def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPostfix(infix):
    stack = []
    output = ""
 
    for s in infix:
        if s.isalnum():
            output += s
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            if s == '^':
                while stack and prec(s) <= prec(stack[-1]):
                    output += stack.pop()
            else:
                while stack and prec(s) < prec(stack[-1]):
                    output += stack.pop()
            stack.append(s)
    while stack:
        output += stack.pop()
    return output
 
def infixToPrefix(infix):
    infix = infix[::-1]
    infix = list(infix)
    for i in range(len(infix)):
        if infix[i] == '(':
            infix[i] = ')'
        elif infix[i] == ')':
            infix[i] = '('
    infix = ''.join(infix)
    prefix = infixToPostfix(infix)
    prefix = prefix[::-1]
    return prefix

exp = 'a+b+c+d-e'
# exp = '3^(1+1)'
exp = 'a^b^c'
print(infixToPrefix(exp))