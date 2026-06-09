class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        maxprod,minprod=1,1
        for n in nums:
            temp=n*maxprod
            maxprod=max(n*maxprod,n*minprod,n)
            minprod=min(n*minprod,temp,n)
            res=max(res,maxprod)
        return res

        