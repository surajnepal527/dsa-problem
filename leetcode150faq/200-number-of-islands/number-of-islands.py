class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [0]
        def dfs(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != "1":
                return
            grid[r][c] = "-1"
            dfs(r+1, c)
            dfs(r-1,c)
            dfs(r, c+1)
            dfs(r,c-1)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res[0] += 1
        return res[0]    