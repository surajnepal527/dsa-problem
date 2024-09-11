class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        t = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(0, 0, m , n, t)
    
    def solve(self, row, col , m , n,t):
        if row >= m or col >= n:
            return 0
        
        if row == m-1 and col == n-1:
            return 1
        
        if t[row][col] != -1:
            return t[row][col]
        
        #go down and go right
        right = self.solve(row+1, col, m , n,t )
        down = self.solve(row, col+1, m , n, t)
        t[row][col] = right + down
        return t[row][col]
        
        