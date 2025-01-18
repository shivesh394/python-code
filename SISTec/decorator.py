# decorator are mainly used to extend the functionality of function

# (function)input--->Decorator is a function--->output(function)


def decor(func):
    def inner(name):
        if name=="Head":
            print("Hello sir welcome")
            print("Nice to meet you")
        else:
            func(name)
    return(inner)
        
@decor
def hello(name):
    print("Hello",name)

hello("Shivesh")
hello("Head")