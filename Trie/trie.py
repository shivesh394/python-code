class Node:
    def __init__(self):
        self.links = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            if s not in cur.links:
                cur.links[s] = Node()
            cur = cur.links[s]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        for s in word:
            if s not in cur.links:
                return False
            else:
                cur = cur.links[s]
        return cur.isEnd 

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for s in prefix:
            if s not in cur.links:
                return False
            else:
                cur = cur.links[s]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)