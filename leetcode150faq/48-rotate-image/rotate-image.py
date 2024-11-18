class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len, col_len = len(matrix), len(matrix[0])
        for r in range(row_len):
            for c in range(r+1, col_len):
                matrix[r][c] , matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in range(row_len):
            start, end = 0 , col_len-1
            while start< end:
                matrix[r][start], matrix[r][end] = matrix[r][end], matrix[r][start]
                start += 1
                end -= 1
        