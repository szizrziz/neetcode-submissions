class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        op=[intervals[0]]
        for start, end in intervals:
            lastend=op[-1][1]
            if start<=lastend:
                op[-1][1]=max(lastend,end)
            else:
                op.append([start,end])
        return op

        