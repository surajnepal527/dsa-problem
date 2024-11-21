class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        output = []
        top, bottom = 0, len(matrix)-1
        left, right = 0 , len(matrix[0])-1
        while top <= bottom and left <= right:
            #left to right on top -->
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1

            #top to bottom on right |
            for j in range(top, bottom+1):
                output.append(matrix[j][right])
            right -= 1

            #right to left on bottom
            if top <= bottom:
                for i in range(right, left-1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1

            #botton to top on left
            if left <= right:
                for j in range(bottom , top-1, -1):
                    output.append(matrix[j][left])
                left += 1

        return output
        
        

        