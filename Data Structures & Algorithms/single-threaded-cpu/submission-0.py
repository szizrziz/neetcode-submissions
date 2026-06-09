class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])
        res,minheap=[],[]
        i,cputime=0,tasks[0][0]
        while minheap or i<len(tasks):
            while i<len(tasks) and cputime >=tasks[i][0]:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                cputime=tasks[i][0]
            else:
                ttime,idx=heapq.heappop(minheap)
                cputime+=ttime
                res.append(idx)
        return res

        