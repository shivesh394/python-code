def prec(c):
    if c == '^':
        return 3
    elif c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPrefix(infix):
    stack = []
    output = ""
 
    for s in reversed(infix):
        if s.isalnum():
            output += s
        elif s == ')':
            stack.append(s)
        elif s == '(':
            while stack[-1] != ')':
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
    return output[::-1]
 

exp = 'a+b+c+d-e'
# exp = '3^(1+1)'
# exp = 'a^b^c'
print(infixToPrefix(exp))