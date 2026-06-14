class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=[1]*n
        for i in range(m-1):
            nextrow=[1]*n
            for j in range(n-2,-1,-1):
                nextrow[j]=row[j]+nextrow[j+1]
            row=nextrow
        return row[0]
        