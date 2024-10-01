class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def solve(r, c, cur):
            if cur == len(word):
                return True
            if (r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in path or board[r][c] != word[cur]):
                return False
            path.add((r,c))
            res = (solve(r+1, c, cur+1) or solve(r-1, c, cur+1) or solve(r, c+1, cur+1) or solve(r, c-1, cur+1))
            path.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if solve(r, c, 0):
                    return True
        return False
        
                
            
            
            