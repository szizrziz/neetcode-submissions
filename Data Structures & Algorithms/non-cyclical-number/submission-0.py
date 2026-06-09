class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = self.findsquare(n),n
        while(fast!=slow):
            fast=self.findsquare(fast)
            fast=self.findsquare(fast)
            slow=self.findsquare(slow)
        if fast == 1: return True
        return False
    def findsquare(self,n:int)->int:
        op=0
        while n:
            digit=n%10
            digit=digit**2
            op+=digit
            n=n//10
        return op
