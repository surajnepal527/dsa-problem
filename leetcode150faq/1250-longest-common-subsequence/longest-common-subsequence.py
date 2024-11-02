class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        tmp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    tmp[i][j] = 1 + tmp[i+1][j+1]
                else:
                    tmp[i][j] = max(tmp[i+1][j], tmp[i][j+1])
        return tmp[0][0]
        