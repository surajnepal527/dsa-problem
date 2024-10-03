class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        res = [0]
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1:
                return 0
            area = 1
            grid[r][c] = -1
            area += dfs(r+1, c)
            area += dfs(r-1, c )
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res[0] = max(res[0],dfs(r, c))
        return res[0]
                
        