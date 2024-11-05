class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1_len, w2_len = len(word1), len(word2)
        memo = {}
        def solve(i, j):
            if i == w1_len: return w2_len - j
            if j == w2_len: return w1_len - i
            if (i,j) in memo: return memo[(i,j)]
            ans = max(w1_len, w2_len)
            if word1[i] == word2[j]:
                ans = solve(i+1, j+1)
            else:
                ans_i = 1 + solve(i, j+1)
                ans_d = 1 + solve(i+1, j)
                ans_r = 1 + solve(i+1, j+1)
                ans = min(ans, ans_i, ans_d, ans_r)
            memo[(i,j)] = ans
            return memo[(i,j)]
        return solve(0,0)

                
        