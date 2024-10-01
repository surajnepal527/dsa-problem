class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def solve(r, c, cur):
            if cur == len(word):
                return True
            if (r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] == "#" or board[r][c] != word[cur]):
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            res = (solve(r+1, c, cur+1) or solve(r-1, c, cur+1) or solve(r, c+1, cur+1) or solve(r, c-1, cur+1))
            board[r][c] = tmp
            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and solve(r, c, 0):
                    return True
        return False
        
                
            
            
            