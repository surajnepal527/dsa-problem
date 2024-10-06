from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a adj list
        adj = defaultdict(list)
        visited = set()
        current_path = set()
        for c,p in prerequisites:
            adj[p].append(c)
        
        def dfs(cur_course):
            if cur_course in current_path:
                return True
            if cur_course in visited:
                return False
            current_path.add(cur_course)
            for prereq in adj[cur_course]:
                if dfs(prereq):
                    return True
            current_path.remove(cur_course)
            visited.add(cur_course)
            return False
        
        for c in range(numCourses):
            if c not in visited:
                if dfs(c):
                    return False
        return True
            
        
        

        