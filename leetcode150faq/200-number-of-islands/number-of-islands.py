class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len , col_len , res = len(grid), len(grid[0]), 0
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r, c):
            if r < 0 or r >= row_len or c < 0 or c >= col_len or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            for dr, dc in drs:
                dfs(dr+r, dc+c)
        
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        
        return res



        