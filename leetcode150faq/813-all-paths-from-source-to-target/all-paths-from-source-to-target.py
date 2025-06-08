class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        output = []

        def dfs(node, path):
            if node == n-1:
                output.append(path[:])
            for nei in graph[node]:
                path.append(nei)
                dfs(nei, path)
                path.pop()
        dfs(0,[0])
        return output
