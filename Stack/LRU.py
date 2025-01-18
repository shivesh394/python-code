class LRUCache:
    class Node:
        def __init__(self, key=None, val = None, next=None, prev=None):
            self.next = next
            self.prev = prev
            self.key = key
            self.val = val
    head = Node(-1, -1)
    last = Node(-1, -1)
    d = {}

    def __init__(self, capacity: int):
        self.size = capacity
        self.head.next = self.last
        self.last.prev = self.head

    def delete(self, cur):
        cur.next.prev = cur.prev
        cur.prev.next = cur.next
    
    def insert(self, cur):
        cur.next = self.head.next
        cur.prev = self.head
        self.head.next.prev = cur
        self.head.next = cur

    def get(self, key: int) -> int:
        if key in self.d:
            ans = self.d[key].val
            cur = self.d[key]
            self.d.pop(key)
            self.delete(cur)
            self.insert(cur)
            self.d[key] = self.head.next
            return ans 
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            cur = self.d[key]
            self.delete(cur)
            self.d.pop(key)
        if self.size == len(self.d):
            self.d.pop(self.last.prev.key)
            self.delete(self.last.prev)

        newNode = self.Node(key, value)
        self.insert(newNode)
        self.d[key] = self.head.next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
capacity = 2
obj = LRUCache(capacity)
obj.put(1, 0)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))