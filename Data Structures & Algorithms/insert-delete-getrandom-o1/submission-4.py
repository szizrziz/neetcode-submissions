class RandomizedSet:

    def __init__(self):
        self.nummap={}
        self.numlist=[]
            
    def insert(self, val: int) -> bool:
        if val in self.nummap:
            return False
        self.nummap[val]=len(self.numlist)
        self.numlist.append(val)
        
    def remove(self, val: int) -> bool:
        if val not in self.nummap:
            return False
        idx=self.nummap[val]
        last=self.numlist[-1]
        self.numlist[idx]=last
        self.nummap[last]=idx
        self.numlist.pop()
        del self.nummap[val]
        return


    def getRandom(self) -> int:
        return random.choice(self.numlist)
        
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()