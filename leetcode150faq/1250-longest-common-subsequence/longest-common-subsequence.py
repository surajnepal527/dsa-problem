class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for _ in range(1001)] for _ in range(1001)]
        def solve(s1, s2, cur_len):
            if s1 >= len(text1) or s2 >= len(text2): return 0
            if memo[s1][s2] != -1: return memo[s1][s2]
            if text1[s1] == text2[s2]:
                count = 1 + solve(s1+1, s2+1, cur_len+1)
            else:
                count = max(solve(s1+1, s2, cur_len), solve(s1, s2+1, cur_len))
            memo[s1][s2] = count
            return memo[s1][s2]
        return solve(0,0,0)


        