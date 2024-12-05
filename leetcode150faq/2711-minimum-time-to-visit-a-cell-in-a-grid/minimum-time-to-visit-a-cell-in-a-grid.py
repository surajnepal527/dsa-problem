class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1: return -1
        min_heap = [(0,0,0)]
        row_len, col_len = len(grid), len(grid[0])
        visited = set()
        while min_heap:
            t, r, c = heapq.heappop(min_heap)
            if (r, c) == (row_len-1, col_len-1): return t
            nei = [(r+1, c), (r-1, c),(r, c+1), (r, c-1)]
            for nr, nc in nei:
                if nr < 0 or nr == row_len or nc < 0 or nc == col_len or (nr, nc) in visited:
                    continue
                wait = 0
                if abs(grid[nr][nc] -t) % 2 == 0:
                    wait = 1
                n_time = max(grid[nr][nc]+wait, t+1)
                heapq.heappush(min_heap,(n_time, nr, nc))
                visited.add((nr, nc))
        