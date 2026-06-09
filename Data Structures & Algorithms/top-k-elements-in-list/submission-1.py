class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,cnt in count.items():
            res[cnt].append(n)
        op=[]
        for i in range(len(res)-1,0,-1):
            for n in res[i]:
                op.append(n)
                if len(op)==k:
                    return op

                



        