class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #idea is to think in reverse way 
        #first mark all the cell on board with O ->NS (T) on it and run dfs for bfs on it
        #mark rest o other to x 
        #rever back T or NS to O
        row_len , col_len = len(board), len(board[0])
        drs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def dfs(r, c):
            if r< 0 or r >= row_len or c < 0 or c >= col_len or (r,c) in visited or board[r][c] != "O":
                return
            board[r][c]= "T"
            visited.add((r,c))
            for dr, dc in drs:
                dfs(r+dr, c+dc)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == "O" and (r in [0, row_len-1] or c in [0 , col_len-1]):
                    dfs(r, c)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] != "T":
                    board[r][c] = "X"
        
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == "T":
                    board[r][c] = "O"
                