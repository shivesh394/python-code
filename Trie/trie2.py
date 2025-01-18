class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] != None
    def putKey(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    def setEnd(self):
        self.flag = True
    def isEnd(self):
        return self.flag
        

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for s in word:
            if not node.containsKey(s):
                node.putKey(s, Node())
            node = node.get(s)
        node.setEnd()



    def search(self, word: str) -> bool:
        node = self.root
        for s in word:
            if not node.containsKey(s):
                return False
            node = node.get(s)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for s in prefix:
            if not node.containsKey(s):
                return False
            node = node.get(s)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)