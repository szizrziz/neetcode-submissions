class Solution:
    def calculate(self, s: str) -> int:
        i=0
        curr=prev=res=0
        cur_operator="+"
        while i < len(s):
            cur_char=s[i]
            if cur_char.isdigit():
                while i<len(s) and s[i].isdigit():
                    curr=curr*10+int(s[i])
                    i+=1
                i-=1
                if cur_operator=="+":
                    res+=curr
                    prev=curr
                elif cur_operator=="-":
                    res-=curr
                    prev=-curr
                elif cur_operator=="*":
                    res-=prev
                    res+=prev*curr
                    prev=prev*curr
                else:
                    res-=prev
                    res+=int(prev/curr)
                    prev=int(prev/curr)
                curr=0
            elif cur_char!=" ":
                cur_operator=cur_char 
            i+=1 
        return res      

        