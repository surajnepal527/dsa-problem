class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(isConnected)
        visited = [False] * n
        for row in range(n):
            if not visited[row]:
                count += 1
                self.dfs(isConnected, row, visited, n)
        
        return count;
    
    def dfs(self, isConnected, row, visited, n):
        visited[row] = True
        for col in range(n):
            if not visited[col] and isConnected[row][col] == 1:
                self.dfs(isConnected, col, visited, n)
    


        