from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        visited = set()
        cur_path = set()
        stack, res = [], []
        def dfs(crs):
            if crs in cur_path:
                return False
            if crs in visited:
                return  True
            cur_path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            stack.append(crs)
            cur_path.remove(crs)
            visited.add(crs)
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):return []
        

        while stack:
            res.append(stack.pop())
        return res

        