class Solution:
    def reorganizeString(self, s: str) -> str:
        count={}
        for c in s:
            count[c]=count.get(c,0)+1
        maxheap=[[-cnt,chr] for chr,cnt in count.items()]
        heapq.heapify(maxheap)
        res=""
        prev=None
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt,chr=heapq.heappop(maxheap)
            res+=chr
            cnt+=1

            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            if cnt!=0:
                prev=[cnt,chr]
        return res
        