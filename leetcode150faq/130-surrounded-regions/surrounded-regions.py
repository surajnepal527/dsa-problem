from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        if rows < 3 and cols < 3:
            return
        que = deque()
        row_col_list = [(1,0),(-1,0),(0,1),(0,-1)]
        #just iterate over boundaries
        def mark_boundries(r, c):
            board[r][c] = "NS"
            que.append((r,c))

        #first row and last row
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == "O":
                    mark_boundries(r,c)

        #first col and last col
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == "O":
                    mark_boundries(r,c)

        while que:
            rq, cq = que.popleft()
            for rl, cl in row_col_list:
                rn, cn = rq+rl, cq+cl
                if 0<= rn < rows and 0<= cn < cols and board[rn][cn] == "O":
                    board[rn][cn] = "NS"
                    que.append((rn, cn))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "NS":
                    board[r][c] = "O"
        
                

        
        