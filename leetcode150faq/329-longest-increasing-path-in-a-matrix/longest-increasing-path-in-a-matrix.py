class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col  = len(matrix), len(matrix[0])
        dr = [(1,0),(0,1),(-1,0),(0,-1)]
        memo = {}
        t_max_len = 1
        def solve(r, c):
            max_len = 1
            if (r,c) in memo:return memo[(r,c)]
            for nr, nc in dr:
                new_r , new_c = r+nr, c+nc
                if 0<= new_r < row and 0<= new_c < col and matrix[r+nr][c+nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + solve(new_r, new_c))
            memo[(r,c)] =  max_len
            return memo[(r,c)]
        
        for r in range(row):
            for c in range(col):
                t_max_len = max(t_max_len, solve(r, c))
        return t_max_len

            
