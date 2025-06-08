from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        queue = deque([])
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    res += 1
                    queue.append((r,c))
                    while queue:
                        qr, qc = queue.popleft()
                        grid[qr][qc] = "0"
                        for dr, dc in drs:
                            nr, nc = qr+dr, qc+dc
                            if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len or grid[nr][nc] != "1":
                                continue
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
                        
        return res