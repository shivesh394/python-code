def outer():
    # print("this is outer function")
    def inner():
        print("this is inner function")
    return (inner)

s=outer()
s()
print(s())