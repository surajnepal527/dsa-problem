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
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows- 1 or c == cols - 1:
                    if board[r][c] == "O":
                        board[r][c] = "NS"
                        que.append((r,c))
                    visited.add((r, c))
        while que:
            rq, cq = que.popleft()
            for rl, cl in row_col_list:
                rn, cn = rq+rl, cq+cl
                if 0<= rn < rows and 0<= cn < cols and (rn, cn) not in visited and board[rn][cn] == "O":
                    board[rn][cn] = "NS"
                    que.append((rn, cn))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "NS":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "NS":
                    board[r][c] = "O"
        
                

        
        