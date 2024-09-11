class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        tmp = [[-1 for _ in range(1001)] for _ in range(1001)]
        return self.solve(0 , 0,text1, text2, tmp)
    
    def solve(self, idx1, idx2, text1, text2, tmp):
        if idx1 >= len(text1) or idx2 >= len(text2):
            return 0
        
        if tmp[idx1][idx2] != -1:
            return tmp[idx1][idx2]

        if text1[idx1] == text2[idx2]:
            tmp[idx1][idx2] = 1 + self.solve(idx1+1, idx2+1, text1, text2,tmp)
           
        else:
           tmp[idx1][idx2] =  max(self.solve(idx1, idx2+1, text1, text2, tmp), self.solve(idx1+1, idx2, text1, text2,tmp)) 

        return tmp[idx1][idx2]            