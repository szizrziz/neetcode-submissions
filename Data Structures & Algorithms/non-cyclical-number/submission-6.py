class Solution:
    def isHappy(self, n: int) -> bool:
        slow,fast=n,self.sq(n)
        while slow!=fast:
            fast=self.sq(fast)
            fast=self.sq(fast)
            slow=self.sq(slow)
        return True if fast==1 else False
    def sq(self,n:int)->int:
        op=0
        while n:
            dig=n%10
            op+=dig**2
            n=n//10
        return op
