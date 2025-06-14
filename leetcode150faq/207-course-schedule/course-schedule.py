class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req_map = {c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            pre_req_map[crs].append(pre)
        
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True
            cycle.add(crs)
            visited.add(crs)
            for nei in pre_req_map[crs]:
                if not dfs(nei): return False
            cycle.remove(crs)
            return True


        for crs in range(numCourses):
            if crs not in visited:
                if not dfs(crs): return False
        
        return True
        