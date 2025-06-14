class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req_map = { c:[] for c in range(numCourses)}
        for crs, req in prerequisites:
            pre_req_map[crs].append(req)
        visited, cycle = set(), set()
        output = []
        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True
            cycle.add(crs)
            visited.add(crs)
            for nei in pre_req_map[crs]:
                if not dfs(nei): return False
            output.append(crs)
            cycle.remove(crs)
            return True

        for c in range(numCourses):
            if c not in visited:
                if not dfs(c): return []
        return output
        