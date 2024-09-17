class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False
        row_len = len(matrix)
        col_len = len(matrix[0])
        #first row check
        for col in range(col_len):
            if matrix[0][col] == 0:
                first_row_zero = True
                break
        #first col check
        for row in range(row_len):
            if matrix[row][0] == 0:
                first_col_zero = True
        #Iterate over the entire matrix and set first row and col to zer
        #as per inter content
        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
        

        for row in range(1, row_len):
            for col in range(1, col_len):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if first_row_zero:
            for col in range(col_len):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(row_len):
                matrix[row][0] = 0

            


    