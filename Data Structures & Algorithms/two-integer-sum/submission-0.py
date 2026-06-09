class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashsum={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashsum:
                return [hashsum[diff],i]
            hashsum[n]=i
        return