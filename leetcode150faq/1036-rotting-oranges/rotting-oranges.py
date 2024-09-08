from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0])
        queue = deque()
        fresh_count = 0
        #lets find first rotten orange
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh_count += 1


        if fresh_count == 0:
            return 0

        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        max_step = 0
        while queue:
            cur_row, cur_col, steps = queue.popleft()
            max_step = max(max_step, steps)
            
            for dr, dc in directions:
                new_row, new_col = dr+cur_row, dc+cur_col
                if 0 <= new_row < row_len and 0 <= new_col < col_len and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, steps+1))
                    fresh_count -= 1

        #check if there are any fresh orange left
        return -1 if fresh_count > 0 else max_step          
        