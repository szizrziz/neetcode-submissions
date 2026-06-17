class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.cirrob(nums[1:]),self.cirrob(nums[:-1]))
    def cirrob(self,nums):
        rob1,rob2=0,0
        for n in nums:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2
        