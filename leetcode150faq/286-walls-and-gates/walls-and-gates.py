from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        row_col_list = [(1,0), (-1,0),(0,1),(0,-1)]
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:                  
                    que.append((r, c))
 
        while que:
            n = len(que)
            for _ in range(n):
                ro, co = que.popleft()
                for r1, c1 in row_col_list:
                    n_r = ro+r1
                    n_c = co+c1
                    if 0 <= n_r < rows and  0 <= n_c < cols and rooms[n_r][n_c] == 2147483647:
                        rooms[n_r][n_c] = rooms[ro][co] + 1
                        que.append((n_r, n_c))
























    