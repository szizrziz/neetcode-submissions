class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[False]*(len(p)+1)
        dp[len(p)]=True
        for i in range(len(s),-1,-1):
            nextdp=[False]*(len(p)+1)
            nextdp[len(p)]=(i==len(s))
            for j in range(len(p)-1,-1,-1):
                match=i<len(s) and (s[i]==p[j] or p[j]==".")
                if (j+1)<len(p) and p[j+1]=="*":
                    nextdp[j]=nextdp[j+2]
                    if match:
                        nextdp[j]|=dp[j]
                elif match:
                        nextdp[j]=dp[j+1]
            dp=nextdp
        return dp[0]


        
                    




        