class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=cursum=0
        prefixsum={0:1} #pefixsum->freq
        for n in nums:
            cursum+=n
            diff=cursum-k
            res+=prefixsum.get(diff,0)
            prefixsum[cursum]=1+prefixsum.get(cursum,0)
        return res
        