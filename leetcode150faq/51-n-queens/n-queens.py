class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ans = []
        board = [["." for _ in range(n)] for _ in range(n) ]
        def backtrack(row, board):
            if row == n:
                 res.append(["".join(board[k]) for k in range(n)])
                 return
            for col in range(n):
                if self.isValid(board, row, col):
                    board[row][col] = "Q"
                    backtrack(row+1, board)
                    board[row][col] = "."
        
        backtrack(0, board)
        return res
    def isValid(self, board:List[str], row:int, col:int):
        rows = len(board)
        cols = len(board[0])
        #is current col valid
        for r in range(row):
            if board[r][col] == "Q":
                return False
        #is top left diagnoal valid
        r = row -1
        c = col -1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        #is top right diagnoal valid
        rr = row -1
        cr = col +1
        while rr >= 0 and cr < len(board):
            if board[rr][cr] == "Q":
                return False
            rr -= 1
            cr +=1 

        return True
