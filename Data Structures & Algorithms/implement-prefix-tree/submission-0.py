class Trienode:
    def __init__(self):
        self.hashtrie={}
        self.endofword=False
class PrefixTree:

    def __init__(self):
        self.root=Trienode()
        
    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.hashtrie:
                cur.hashtrie[c]=Trienode()
            cur=cur.hashtrie[c]
        cur.endofword=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.hashtrie:
                return False
            cur=cur.hashtrie[c]
        return cur.endofword


    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.hashtrie:
                return False
            cur=cur.hashtrie[c]
        return True
        
        