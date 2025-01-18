class Node:
    def __init__(self, key = None, val = None, next = None, prev = None):
        next = next
        prev = prev
        self.key = key
        self.val = val

head = Node(-1, -1)
print(head.val)