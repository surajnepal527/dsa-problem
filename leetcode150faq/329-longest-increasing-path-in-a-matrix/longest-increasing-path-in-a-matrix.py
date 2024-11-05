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
                if r+nr >= 0 and c + nc >= 0 and r + nr < row and c + nc < col and matrix[r+nr][c+nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + solve(r+nr, c+nc))
            memo[(r,c)] =  max_len
            return memo[(r,c)]
        
        for i in range(row):
            for j in range(col):
                t_max_len = max(t_max_len, solve(i, j))
        return t_max_len

            
