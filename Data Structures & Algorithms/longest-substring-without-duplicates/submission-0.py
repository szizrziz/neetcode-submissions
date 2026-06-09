class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in longset:
                longset.remove(s[l])
                l+=1
            longset.add(s[r])
            res=max(res,r-l+1)
        return res

        