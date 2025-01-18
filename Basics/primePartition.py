def factor(n):
  factorlist=[]
  for i in range(1,n+1):
    if n%i==0:
      factorlist=factorlist+[i]
  return factorlist 
  
def isprime(n):
  return (factor(n)==[1,n])

def primeupto(n):
  primelist=[]
  for i in range(1,n+1):
    if isprime(i):
      primelist=primelist+[i]
  return primelist


def primepartition(m):
    if m<0:
        return False
    l=primeupto(m)
    # print(l)
    count=0
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if(m==(l[i]+l[j])):
                count=1
                print(l[i],l[j])
                return True
    if(count!=1):
        return False      
n=int(input())
print(primepartition(n))