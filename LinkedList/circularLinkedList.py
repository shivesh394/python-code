class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def insertBegin(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
    
    # def insertEnd(self, data):
    #     node = Node(data)
    #     if not self.head:
    #         self.head = node
    #         self.tail = node
    #     else:
    #         cur = self.head
    #         while cur.next != self.head:
    #             cur = cur.next
    #         cur.next = node
    #         node.next = self.head
    #         self.tail = node

    def insertEnd(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:        
            self.tail.next = node
            node.next = self.head
            self.tail = node

    def deleteBegin(self):
        self.tail.next = self.head.next
        self.head = self.head.next
    
    def deleteEnd(self):
        if not self.head:
            return
        cur = self.head
        while cur.next.next != self.head:
            cur = cur.next
        cur.next = cur.next.next
        self.tail = cur.next
    
    def display(self):
        cur = self.head
        while cur.next != self.head:
            print(cur.data, end = '->')
            cur = cur.next
        print(cur.data)

obj = CircularLinkedList()
obj.insertBegin(10)
obj.insertBegin(20)
obj.insertBegin(30)
obj.insertBegin(40)
obj.display()
obj.insertEnd(100)
obj.insertEnd(200)
obj.insertEnd(300)
obj.insertEnd(400)
obj.display()
obj.deleteBegin()
obj.display()
obj.deleteEnd()
obj.deleteEnd()
obj.display()
