from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, res = len(grid), len(grid[0]), 0
        que = deque()
        def dfs():
            while que:
                pr, pc = que.popleft()
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = pr+dr, pc+dc
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or grid[nr][nc] != "1":
                        continue
                    grid[nr][nc] = "-1"
                    que.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    grid[r][c] = "-1"
                    que.append((r,c))
                    dfs()
                    res += 1
        return res
        
        
        