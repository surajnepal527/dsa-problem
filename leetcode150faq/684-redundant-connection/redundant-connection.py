class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = {i:i for i in range(1, n)}
        rank = {i:0 for i in range(1, n)}

        def find(i:int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(x : int, y : int) -> int:
            x_p, y_p = find(x), find(y)
            if x_p == y_p:
                return False
            if rank[x_p] > rank[y_p]:
                parent[y_p] = x_p
            elif rank[y_p] > rank[x_p]:
                parent[x_p] = y_p
            else:
                parent[x_p] = y_p
                rank[y_p] += 1
            return True
        
        for u, v in edges:
            if not union(u, v) : return [u, v]


        