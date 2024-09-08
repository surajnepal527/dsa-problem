from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        row_len = len(maze)
        col_len = len(maze[0])
        #visited = [[False for _ in range(col_len)] for _ in range(row_len)]
        queue = deque([(entrance[0], entrance[1], 0)])
        #visited[entrance[0]][entrance[1]] = True
        directions = [(-1,0), (0,1),(1,0),(0, -1)]
        while queue:
            cur_row, cur_col, steps = queue.popleft()
            if self.checkBoundaries(cur_row, cur_col, maze) and (cur_row != entrance[0] or cur_col != entrance[1]):
                return steps
            
            for dr, dc in directions:
                new_row, new_col = cur_row + dr, cur_col + dc
                if 0 <= new_row < row_len and 0 <= new_col < col_len and maze[new_row][new_col] != "+":
                    maze[new_row][new_col] = "+"
                    queue.append((new_row, new_col, steps+1))
        
        return -1



    def checkBoundaries(self, row, col, maze):
        return row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) -1
        