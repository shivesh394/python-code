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
  count=0
  for i in range(0,len(l)):
      for j in range(i,len(l)):
          if(m==(l[i]+l[j])):
              count=1
              return True
  if(count!=1):
      return False          
  
  
  
  
  
def matched(s):
  count=0
  pos1=[]
  pos2=[]
  for i in range(0,len(s)):
    if(s[i]=="(" ):
      count=count+1
      pos1.append(i)
    if(s[i]==")" ):
      count=count+1 
      pos2.append(i)
  if(count%2==0 and pos1[0]<pos2[0]):
    return True
  else:
    return False







def rotatelist(l,k):
  l=l[k%5:]+l[:k%5]
  return l