def prefixToPostfix(string):
    stack = []
    for s in reversed(string):
        if s.isalnum():
            stack.append(s)
        else:
            a = stack.pop()
            b = stack.pop()
            res = a + b + s
            stack.append(res)
    return stack[-1]

string = '*-a/bc-/dkl'
string = '-+2*34/2^23'
print(prefixToPostfix(string))