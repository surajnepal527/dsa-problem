class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col  = len(matrix[0])
        left = 0
        right = (row*col)-1
        while left <= right:
            mid = (left + right) // 2
            cur_row = mid // col
            cur_col = mid % col
            if matrix[cur_row][cur_col] > target:
                right = mid -1
            elif matrix[cur_row][cur_col] < target:
                left = mid +1
            else:
                return True
        
        return False

