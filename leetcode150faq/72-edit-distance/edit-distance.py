class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1), len(word2)
        t = [[-1 for _ in range(502)] for _ in range(502)]
        return self.solve(0,0,word1, word2, t)
    
    def solve(self, idx1, idx2, w1, w2, t):
        if idx1 >= len(w1):
            return len(w2)- idx2
        
        if idx2 >= len(w2):
            return len(w1) - idx1
        
        if t[idx1][idx2] != -1:
            return t[idx1][idx2]

        if w1[idx1] == w2[idx2]:
          t[idx1][idx2] = self.solve(idx1+1, idx2+1, w1, w2, t)
          return t[idx1][idx2]
        else:
            replace = 1 + self.solve(idx1+1, idx2+1, w1, w2, t)
            delete = 1 + self.solve(idx1+1, idx2, w1, w2, t)
            insert = 1 + self.solve(idx1, idx2+1, w1, w2, t)
            t[idx1][idx2] =  min(replace, delete, insert)
            return t[idx1][idx2]
        
        return -1
        
           
        