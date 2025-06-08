from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #multisource BFS , there might be multiple orange that can work togher and queue will hep us for that b processing simlatnously
        row_len, col_len = len(grid), len(grid[0])
        mt = 0
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh_count = 0
        queue = deque()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    queue.append((r,c))
        while queue and fresh_count:
            level = len(queue)
            for i in range(level):
                qr, qc = queue.popleft()
                for dr, dc in drs:
                    nr, nc = dr+qr, dc+qc
                    if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    fresh_count -= 1
            mt += 1
        return mt if fresh_count == 0 else -1

