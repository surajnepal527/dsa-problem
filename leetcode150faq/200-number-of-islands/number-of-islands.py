class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, res = len(grid),len(grid[0]),0
        drs = [(1,0),(-1,0),(0,1),(0,-1)]
        def solve(r, c):
            for dr, dc in drs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != "1":
                    continue
                grid[nr][nc] = "0"
                solve(nr, nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    solve(r,c)
                    res += 1
        return res