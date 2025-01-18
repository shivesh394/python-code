front=-1
rear=-1
queue=[]
def enqueue():
    global rear
    global front
    if(rear==5):
        # print("Overflow")
        return
    else:
        if front==-1:
            front=0
        rear+=1
        n=int(input("Enter a number :"))
        queue.insert(rear, n)

def dequeue():
    global front
    if(front==-1):
        print("Underflow")
    else:
        print(queue[front]," is deleted")
        front-=1
    if front>rear:
        front=-1
        rear=-1

def display():
    global front
    if(front==-1):
        print("Underflow")
    for i in range(front,rear+1):
        print(queue[i])

enqueue()
enqueue()
enqueue()
enqueue()
enqueue()
enqueue()

display()