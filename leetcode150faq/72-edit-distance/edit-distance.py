class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n  = len(word1), len(word2)
        t = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    t[i][j] = i + j
                elif word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1]
                else:
                    t[i][j] = 1+ min(t[i][j-1],t[i-1][j], t[i-1][j-1])
        
        return t[m][n]