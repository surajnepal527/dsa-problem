class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        tmp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    tmp[i][j] = 1 + tmp[i-1][j-1]
                else:
                    tmp[i][j] = max(tmp[i-1][j], tmp[i][j-1])
        
        return tmp[len(text1)][len(text2)]
