class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = 0
        output = []
        while(row > 1 and col > 1):

            for k in range(col - 1):
                output.append(matrix[i][j])
                j += 1
            for k in range(row - 1):
                output.append(matrix[i][j])
                i += 1
            for k in range(col - 1):
                output.append(matrix[i][j])
                j -= 1
            for k in range(row - 1):
                output.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            row -= 2
            col -= 2
        
        if row == 1 and col > 1:
            for k in range(col):
                output.append(matrix[i][j])
                j += 1
        if row > 1 and col == 1:
            for k in range(row):
                output.append(matrix[i][j])
                i += 1
        elif row == 1 and col == 1:
            output.append(matrix[i][j])
        
        return output
        