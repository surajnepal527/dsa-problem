from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid),len(grid[0])
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        queue = deque()
        max_count = 0
        fresh_count = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        while queue and fresh_count > 0:
            qr, qc , step = queue.popleft()
            for dr, dc in drs:
                nr, nc = qr+dr, qc+dc
                if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len or grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = 2
                queue.append((nr,nc,step+1))
                fresh_count -= 1
                max_count = max(max_count,step+1)
        return max_count if fresh_count == 0 else -1
