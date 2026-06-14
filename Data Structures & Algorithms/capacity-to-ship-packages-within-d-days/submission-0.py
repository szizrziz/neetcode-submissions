class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        def iscap(cap):
            ships,currcap=1,cap
            for w in weights:
                if currcap-w<0:
                    ships+=1
                    currcap=cap
                currcap-=w
            return ships<=days
        while l<=r:
            cap=(l+r)//2
            if iscap(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res