class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #initialize board
        board = [["." for _ in range (n)] for _ in range(n)]
        res, col_set, left_dia_set, right_dia_set = [], set(), set(),set()
        def backtrack(row):
            if row == n:
                res.append(["".join(board[k]) for k in range(n)])
            for col in range(n):
                if col not in col_set and (row-col) not in left_dia_set and (row+col) not in right_dia_set:
                    board[row][col]= "Q"
                    col_set.add(col)
                    left_dia_set.add(row-col)
                    right_dia_set.add(row+col)
                    backtrack(row+1)
                    board[row][col]= "."
                    col_set.remove(col)
                    left_dia_set.remove(row-col)
                    right_dia_set.remove(row+col)
            
        backtrack(0)
        return res
        