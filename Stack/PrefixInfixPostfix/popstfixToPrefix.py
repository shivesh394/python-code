def postfixToPrefix(string):
    stack = []
    for s in (string):
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            res = s + b + a
            stack.append(res)
    return stack[-1]

string = 'abc/-dk/l-*'
print(postfixToPrefix(string))