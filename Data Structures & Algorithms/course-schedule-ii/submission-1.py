class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cmap={c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            cmap[crs].append(pre)
        visiting=set() #tracks cycles
        visited=set() #track nodes that are visited
        op=[] #op list
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for pre in cmap[crs]:
                if dfs(pre)==False:
                    return False
            visiting.remove(crs)
            visited.add(crs)
            op.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c)==False:
                return []
        return op

                


        