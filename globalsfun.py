a=100
def f1():
    a=77
    print(a)
    print(globals()['a'])
    globals()['a']=19
    print(globals()['a'])
    print(a)

f1()