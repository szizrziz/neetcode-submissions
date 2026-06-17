class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:
    def __init__(self, capacity: int):
      self.capacity=capacity  
      self.cache={} #key->node

      #ptr to least freq used and most freq used
      self.left, self.right=Node(0,0),Node(0,0)

      #connecting both the nodes
      self.left.next=self.right
      self.right.prev=self.left
    
    #remove 
    def remove(self,node):
        #prev and nxt are my 2 left and right nodes which im trying
        #to retrieve from node
        prv,nxt=node.prev,node.next
        prv.next=nxt
        nxt.prev=prv

    #add to right
    def insert(self,node):
        #prev and nxt are my 2 left and right nodes which im trying
        #to retrieve from my "right" node
        prv,nxt=self.right.prev,self.right
        prv.next=nxt.prev=node
        node.next=nxt
        node.prev=prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            leastused=self.left.next
            self.remove(leastused)
            del self.cache[leastused.key]
