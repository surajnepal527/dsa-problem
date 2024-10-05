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
        visited = set()
        row_col_list = [(1,0),(-1,0),(0,1),(0,-1)]
        #just iterate over boundaries
        #first row and last row
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "NS"
                que.append((0,c))
            if board[rows-1][c] == "O":
                board[rows-1][c] = "NS"
                que.append((rows-1,c))
        #first col and last col
        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "NS"
                que.append((r, 0))
            if board[r][cols-1] == "O":
                board[r][cols-1] = "NS"
                que.append((r,cols-1))

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
        
                

        
        