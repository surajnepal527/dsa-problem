class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [[-1 for _ in range(1001)] for _ in range(1001)]
        s_idx = -1
        max_len = -1

        def solve(i, j):
            if i >= j:
                return 1
            if memo[i][j] != -1: return memo[i][j]
            if s[i] == s[j]:
                memo[i][j] =  solve(i+1, j-1)
                return memo[i][j]
            else:
                memo[i][j] = 0
                return memo[i][j]
        
        for i in range(len(s)):
            for j in range(len(s)):
                    if solve(i,j) == 1:
                        if j-i+1 > max_len:
                            max_len = j-i+1
                            s_idx = i
        return s[s_idx:s_idx+max_len]
                        

