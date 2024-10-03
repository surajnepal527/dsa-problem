class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid), len(grid[0])
        res = 0
        def dfs(r, c, cur_area):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] != 1:
                return
            cur_area[0] += 1
            grid[r][c] = -1
            dfs(r+1, c, cur_area)
            dfs(r-1, c, cur_area )
            dfs(r, c+1, cur_area)
            dfs(r, c-1, cur_area)
    

        for r in range(rows):
            for c in range(cols):
                cur_area = [0]
                if grid[r][c] == 1:
                    dfs(r, c, cur_area)
                    res = max(res, cur_area[0])
                    
        return res
                
        