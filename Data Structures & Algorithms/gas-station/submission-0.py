class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx=0
        curr_tank=0
        if sum(gas)<sum(cost):
            return -1
        for i in range(len(gas)):
            curr_tank+=gas[i]-cost[i]
            if curr_tank<0:
                curr_tank=0
                idx=i+1

        return idx

