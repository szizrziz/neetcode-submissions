class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longset=set(nums)
        longest=0
        for n in nums:
            if (n-1) not in longset:
                length=0
                while (n+length) in longset:
                    length+=1
                longest=max(longest,length)
        return longest



        