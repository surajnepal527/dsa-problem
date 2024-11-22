class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len , col_len = len(matrix), len(matrix[0])
        isFirstRowZero = False
        isFirstColZero = False
        #check if first row/col have zeros:
        for col in range(col_len):
            if matrix[0][col] == 0:
                isFirstRowZero = True
                break
        for row in range(row_len):
            if matrix[row][0] == 0:
                isFirstColZero = True
                break
        #use First Row and col to store value of corresponding row and col if zero exist
        for row in range(1,row_len):
            for col in range(1, col_len):
                if matrix[row][col] == 0:
                    matrix[0][col], matrix[row][0] = 0, 0
        #set entire row and col to zero if first row or first col is zero
        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        #set first row and col to zero
        if isFirstRowZero:
            for col in range(col_len):
                matrix[0][col] = 0
        if isFirstColZero:
            for row in range(row_len):
                matrix[row][0] = 0
        
        

        


