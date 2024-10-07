from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = defaultdict(list)
        visited = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(u,par):
            if u in visited:
                return False
            visited.add(u)
            for v in adj[u]:
                if v == par:
                    continue

                if not dfs(v, u): return False
            return True
            
        return dfs(0, -1) and len(visited) == n
                    


        