class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        for i in range(len(s)):
            if s[i]!=']':
                st.append(s[i])
            else:
                substr=""
                while st and st[-1]!='[':
                    substr=st.pop()+substr
                st.pop()
                dig=""
                while st and st[-1].isdigit():
                    dig=st.pop()+dig
                st.append(int(dig)*substr)
        return "".join(st)
            




        