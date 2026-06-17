class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        st=[]
        res=[]
        def xyz(openx,closex):
            if openx==closex==n:
                res.append("".join(st))
                return
            if openx<n:
                st.append("(")
                xyz(openx+1,closex)
                st.pop()
            if closex<openx:
                st.append(")")
                xyz(openx,closex+1)
                st.pop()
        xyz(0,0)
        return res        

        