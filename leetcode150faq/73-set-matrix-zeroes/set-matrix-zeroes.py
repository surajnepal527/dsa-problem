class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        false_matrix = [[False] * cols for _ in range(rows)]
        for row in range (rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    false_matrix[row][col] = True
        
        for row in range(rows):
            for col in range(cols):
                if false_matrix[row][col] == True:
                    false_matrix[row][col] == False
                    self.setRowColZeros(matrix, row, col)
        
        return matrix


    def setRowColZeros(self, matrix, row, col):
        #set top to zero
        initTop = row
        initBottom = row
        initLeft = col
        initRight = col
        while initTop >= 0:
            matrix[initTop][col] = 0
            initTop -= 1
        while initBottom < len(matrix):
            matrix[initBottom][col] = 0
            initBottom += 1
        while initLeft >= 0:
            matrix[row][initLeft] = 0
            initLeft -= 1
        while initRight < len(matrix[0]):
            matrix[row][initRight] = 0
            initRight += 1
