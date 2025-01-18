class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertBegin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def insertEnd(self, data):
        node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    
    def insertAnyPosition(self, data, n):
        cur = self.head
        node = Node(data)
        if n == 1:
            node.next = cur
        else:
            while n - 2:
                cur = cur.next
                n -= 1
            node.next = cur.next
            cur.next = node


    def deleteBegin(self):
        self.head = self.head.next


    def deleteEnd(self):
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    
    def display(self):
        cur = self.head
        while cur.next:
            print(cur.data, end = '->')
            cur = cur.next
        print(cur.data)

obj = SinglyLinkedList()
obj.insertBegin(10)
obj.insertBegin(20)
obj.insertBegin(30)
obj.insertBegin(40)
obj.insertEnd(100)
obj.insertEnd(200)
obj.insertEnd(300)
obj.insertEnd(400)
obj.display()
obj.deleteBegin()
obj.deleteEnd()
obj.insertAnyPosition(1000, 4)
obj.display()