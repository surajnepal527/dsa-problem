from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited = set()
        cur_path = set()

        def dfs(cur_crs, cur_path):
            if cur_crs in cur_path:
                return False
            if cur_crs in visited:
                return True
            cur_path.add(cur_crs)
            for pre in adj[cur_crs]:
                if not dfs(pre, cur_path) : return False
            cur_path.remove(cur_crs)
            visited.add(cur_crs)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i, cur_path) : return False
        return True

        