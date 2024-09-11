class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        tmp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    tmp[i][j] = 1
                else:
                    tmp[i][j] = tmp[i-1][j] + tmp[i][j-1]
        
        return tmp[m-1][n-1]
        