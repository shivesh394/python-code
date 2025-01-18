import sys
import random,time
l=[x for x in range(1000)]  #list comprehension
print(type(l))
print(sys.getsizeof(l))
# print(l)

l1=(x for x in range(1000)) #generator
print(type(l1))
print(sys.getsizeof(l1))
# for i in range(1000):
#     print(next(l1))


names=['sk','dk','sp','fg']
subjects=['hindi','eng','maths','science']
def peop_list(num):
    result=[]
    for i in range(num):
        person={'id':i,'name':random.choice(names),'subject':random.choice(subjects)}
        result.append(person)
    return(result)

def peop_gen(num):
    result=[]
    for i in range(num):
        person={'id':i,'name':random.choice(names),'subject':random.choice(subjects)}
        yield person

t1=time.time_ns()
p=peop_list(1000)
t2=time.time_ns()
print("Time",t2-t1)

t3=time.time_ns()
p=peop_gen(10000000000000000000000000)
t4=time.time_ns()
print("Time",t4-t3)