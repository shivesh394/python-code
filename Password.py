import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbol="*_&%$#@"

all=lower+upper+numbers+symbol
length=10
for i in range(1,100):
    password="".join(random.sample(all,length))
    print(password)