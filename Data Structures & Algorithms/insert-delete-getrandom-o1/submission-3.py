class RandomizedSet:

    def __init__(self):
        self.numap={}
        self.numlist=[]   
        
    def insert(self, val: int) -> bool:
        if val in self.numap:
            return False
        self.numap[val]=len(self.numlist)
        self.numlist.append(val)
        return True
             
    def remove(self, val: int) -> bool:
        if val not in self.numap:
            return False
        idx=self.numap[val]
        last=self.numlist[-1]
        self.numlist[idx]=last
        self.numap[last]=idx
        self.numlist.pop()
        del self.numap[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.numlist)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()