class Solution:
    def countSubstrings(self, s: str) -> int:
        l,r=0,len(s)-1
        res=0
        for i in range(len(s)):
            res+=self.palin(s,i,i) #To track odd len substrings
            res+=self.palin(s,i,i+1) #To track even len substrings
        return res
    def palin(self,s,l,r):
        res=0
        while l>=0 and r<len(s) and s[l]==s[r]:
            res+=1  
            l-=1
            r+=1
        return res
                 
        