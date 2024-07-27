class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        row = 0 
        col = 0
        up = True
        ans = []
        while row < m and col < n:
            if up:
                while row > 0 and col < n - 1:
                    ans.append(mat[row][col])
                    row -= 1
                    col += 1
                ans.append(mat[row][col])
                if col == n - 1:
                    row += 1
                else:
                    col += 1
            else:
                while row < m - 1 and col > 0:
                    ans.append(mat[row][col])
                    row += 1
                    col -= 1
                ans.append(mat[row][col])
                if row == m-1:
                    col += 1
                else:
                    row += 1
            up = not up

        return ans

                    

