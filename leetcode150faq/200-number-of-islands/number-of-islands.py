from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        row_len, col_len = len(grid), len(grid[0])
        res = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    res += 1
                    queue = deque([(r,c)])
                    while queue:
                        qr, qc = queue.popleft()
                        for dr, dc in drs:
                            nr, nc = qr+dr, qc+dc
                            #main part of the code
                            #boundary conditin and #is there land if not ignore
                            if nr < 0 or nr >= row_len or nc<0 or nc>= col_len or grid[nr][nc] != "1":
                                continue
                            grid[nr][nc] = "0"
                            queue.append((nr, nc))
        
        return res


        