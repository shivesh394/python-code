class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = None 
        self.prev = prev

class doublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertBegin(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insertEnd(self, data):
        cur = self.head
        node = Node(data)
        while cur.next:
            cur = cur.next
        node.prev = cur
        cur.next = node

    def deleteBegin(self):
        self.head = self.head.next
        self.head.prev = None

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

obj = doublyLinkedList()
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
obj.display()
obj.deleteEnd()
obj.display()