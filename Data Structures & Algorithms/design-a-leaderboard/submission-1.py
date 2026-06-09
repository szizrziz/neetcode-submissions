class Leaderboard:

    def __init__(self):
        self.scores={} #playerid->scores
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId]=0
        self.scores[playerId]+=score
        
    def top(self, K: int) -> int:
        heap=[]
        for i in self.scores.values():
            heapq.heappush(heap,i)
            if len(heap)>K:
                heapq.heappop(heap)
        sum=0
        while heap:
            sum+=heapq.heappop(heap)
        return sum

    def reset(self, playerId: int) -> None:
        self.scores[playerId]=0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
