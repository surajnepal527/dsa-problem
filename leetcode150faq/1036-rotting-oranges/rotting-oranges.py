from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_col_list = [(-1,0),(1,0),(0,-1), (0,1)]
        que = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    que.append((r,c,0))
                if grid[r][c] == 1:
                    fresh_count += 1
        mt = 0
        while que and fresh_count > 0:
            ro, co, t = que.popleft()
            for r1, c1 in row_col_list:
                r_n = ro + r1
                c_n = co + c1
                if 0 <= r_n < rows and 0 <= c_n < cols and grid[r_n][c_n] == 1:
                    grid[r_n][c_n] = 2
                    que.append((r_n, c_n,t+1))
                    fresh_count -= 1
                    mt = max(mt, t+1)

        return mt if fresh_count == 0 else -1
        