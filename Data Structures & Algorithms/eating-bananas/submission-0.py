class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            hour=0
            mid=(l+r)//2
            for p in piles:
                hour+=math.ceil(p/mid)
            if hour<=h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res


        