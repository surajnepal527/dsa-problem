class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #First col matrix matrix[0][col]
        #First row matrix matrix[row][0] 
        rows = len(matrix)
        cols = len(matrix[0])

                #check for row 0
        setRow = False
        for row in range(rows):
            if matrix[row][0] == 0:
                setRow = True
                continue

        setCol = False
        for col in range(cols):
            if matrix[0][col] == 0:
                setCol = True
                continue

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0


        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        

        
        if setRow == True:
            for row in range(rows):
                matrix[row][0] = 0
        
        if setCol == True:
            for col in range(cols):
                matrix[0][col] = 0
        
        return matrix





        