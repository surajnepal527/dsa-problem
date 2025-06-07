class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        def dfs(row:int, col:int):
            if row < 0 or col < 0 or row >= row_len or col >= col_len or grid[row][col] != "1":
                return
            grid[row][col] = "0"
            for dr,dc in drs:
                dfs(row+dr, col+dc) 
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)
        return res