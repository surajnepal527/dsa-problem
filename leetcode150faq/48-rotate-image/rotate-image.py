class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #90 degree roation of a matrix is nothing but combinatation of Transpose and reverse of each row
        #Tanspose given matrix
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[0])):
                self.swap(matrix, row, col)
        
        # now I need to reverse each row
        for row in range(len(matrix)):
            self.reverse(matrix, row)
        

    def reverse(self, matrix, row):
        startCol = 0
        endCol = len(matrix) - 1
        while startCol < endCol:
            tmp = matrix[row][startCol]
            matrix[row][startCol] = matrix[row][endCol]
            matrix[row][endCol] = tmp
            startCol += 1
            endCol -= 1

    def swap(self, matrix, row, col):
        tmp = matrix[row][col]
        matrix[row][col] = matrix[col][row]
        matrix[col][row] = tmp
