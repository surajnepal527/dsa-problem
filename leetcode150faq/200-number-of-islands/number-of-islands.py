from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, res = len(grid), len(grid[0]), 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    que.append((r,c))
                    grid[r][c] = "0"
                    while que:
                        pr, pc = que.popleft()
                        for dr, dc in directions:
                            nr, nc = pr+dr, pc+dc
                            if nr < 0 or nc< 0 or nr == rows or nc == cols or grid[nr][nc] != "1":
                                continue
                            que.append((nr, nc))
                            grid[nr][nc] = "0"
        return res


