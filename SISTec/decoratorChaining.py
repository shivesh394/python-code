def decor1(func):
    def inner():
        x=func() #--->10
        return(x*x)  #--->100
    return(inner)

def decor2(func):
    def inner():
        x=func() #--->100
        return(2*x)  #--->200
    return(inner)



@decor2  #---->third
@decor2  #---->second
@decor1  #---->first execute


def num():
    return(10)

print(num())