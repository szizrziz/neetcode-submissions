class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st=[]
        n=len(heights)
        res=[0]*n
        for i in range(n-1,-1,-1):
            visible=0
            while st and heights[i]>st[-1]:
                visible+=1
                st.pop()
            if st:
                visible+=1
            res[i]=visible
            st.append(heights[i])
        return res
        