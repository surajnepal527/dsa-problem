
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(u, pre):
            visited.add(u)
            for v in adj[u]:
                if v == pre or v in visited:
                    continue
                dfs(v, u)
            return True
        
        cmpt = 0
        for i in range(n):
            if i not in visited:
                cmpt += 1
                if dfs(i, -1) and len(visited) == n:
                    return cmpt

        