class Solution:
    def maxDepth(self, s: str) -> int:
        curr_depth=0
        max_depth=0
        for c in s:
            if c=='(':
                curr_depth+=1
                if curr_depth>max_depth:
                    max_depth=curr_depth
            elif c==')':
                curr_depth-=1
        return max_depth
        